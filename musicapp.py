import sys
import vlc
from pytube import YouTube
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit, QLabel
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# Veritabanı bağlantısı
DATABASE_URL = "postgresql://username:password@localhost:5432/music_app"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Veritabanı Tabloları
class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    added_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

# Ana Uygulama Arayüzü
class MusicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Müzik Uygulaması")
        self.setGeometry(300, 100, 600, 400)

        # VLC Player
        self.player = vlc.MediaPlayer()

        # Arayüz Bileşenleri
        self.layout = QVBoxLayout()
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("YouTube URL'si giriniz")
        self.add_button = QPushButton("Şarkı Ekle")
        self.playlist = QListWidget()
        self.play_button = QPushButton("Oynat")
        self.stop_button = QPushButton("Durdur")
        self.status_label = QLabel("Durum: Beklemede")

        # Bileşenleri Yerleştir
        self.layout.addWidget(self.url_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.playlist)
        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.status_label)
        self.setLayout(self.layout)

        # Event Bağlantıları
        self.add_button.clicked.connect(self.add_song)
        self.play_button.clicked.connect(self.play_song)
        self.stop_button.clicked.connect(self.stop_song)
        self.load_songs()

    def load_songs(self):
        """Veritabanından şarkıları yükler."""
        self.playlist.clear()
        songs = session.query(Song).all()
        for song in songs:
            self.playlist.addItem(f"{song.id} - {song.name}")

    def add_song(self):
        """Şarkı ekleme fonksiyonu."""
        url = self.url_input.text()
        if url:
            yt = YouTube(url)
            song_name = yt.title
            new_song = Song(name=song_name, url=url)
            session.add(new_song)
            session.commit()
            self.load_songs()
            self.url_input.clear()
            self.status_label.setText(f"Eklendi: {song_name}")

    def play_song(self):
        """Seçili şarkıyı oynatır."""
        selected_item = self.playlist.currentItem()
        if selected_item:
            song_id = int(selected_item.text().split(" - ")[0])
            song = session.query(Song).filter_by(id=song_id).first()
            if song:
                yt = YouTube(song.url)
                stream = yt.streams.filter(only_audio=True).first()
                self.player.set_mrl(stream.url)
                self.player.play()
                self.status_label.setText(f"Oynatılıyor: {song.name}")

    def stop_song(self):
        """Şarkıyı durdurur."""
        self.player.stop()
        self.status_label.setText("Durum: Durduruldu")

# Uygulama Çalıştırma
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicApp()
    window.show()
    sys.exit(app.exec_())