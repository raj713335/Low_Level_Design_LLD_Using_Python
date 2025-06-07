class MediaPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def stop_audio(self):
        raise NotImplementedError

    def play_video(self, video_file):
        raise NotImplementedError

    def stop_video(self):
        raise NotImplementedError

    def adjust_audio_volume(self, volume):
        raise NotImplementedError

    def adjust_video_brightness(self, brightness):
        raise NotImplementedError


class AudioPlayer:
    def play_audio(self, audio_file):
        raise NotImplementedError

    def stop_audio(self):
        raise NotImplementedError

    def adjust_audio_volume(self, volume):
        raise NotImplementedError


class VideoPlayer:
    def play_video(self, video_file):
        raise NotImplementedError

    def stop_video(self):
        raise NotImplementedError

    def adjust_video_brightness(self, brightness):
        raise NotImplementedError


class MP3Player(AudioPlayer):
    def play_audio(self, audio_file):
        # Play MP3 file
        pass

    def stop_audio(self):
        # Stop MP3 file
        pass

    def adjust_audio_volume(self, volume):
        # Adjust Volume
        pass


class AviVideoPlayer(VideoPlayer):
    def play_video(self, video_file):
        # Play video
        pass

    def stop_video(self):
        # Stop video
        pass

    def adjust_video_brightness(self, brightness):
        # Adjust Video brightness
        pass


class MultimediaPlayer(AudioPlayer, VideoPlayer):
    # Implements all the methods
    pass