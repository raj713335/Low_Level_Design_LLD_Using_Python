# Subsystem: Complex Video conversion Library

class VideoFile:
    def __init__(self, filename):
        self.filename = filename
        print(f"[VideoFile] Loaded video file: {filename}")


class OggCompressionCodec:
    def __str__(self):
        return "OggCompressionCodec"


class MPEG4CompressionCodec:
    def __str__(self):
        return "MPEG4CompressionCodec"


class CodecFactory:
    def extract(self, file: VideoFile):
        print(f"[CodecFactory] Extracting codec from {file.filename}")
        return OggCompressionCodec() if file.filename.endswith(".ogg") else MPEG4CompressionCodec()


class BitrateReader:
    @staticmethod
    def read(filename: str, codec):
        print(f"[BitrateReader] Reading from {filename} with codec {codec}")
        return f"Buffered_data_from_{filename}"

    @staticmethod
    def convert(buffer: str, codec):
        print(f"[BitrateReader] Converting buffer with {codec}")
        return f"converted_data_to_{codec}"


class AudioMixer:
    def fix(self, result: str):
        print(f"[AudioMixer] Fixing audio in result")
        return f"audio_fixed_{result}"


# Facade

class VideoConverter:
    def convert(self, filename: str, format: str):
        print(f"\n[VideoConverter] Starting conversion of {filename} to {format}")

        file = VideoFile(filename)
        source_codec = CodecFactory().extract(file)

        if format == "mp4":
            destination_codec = MPEG4CompressionCodec()
        else:
            destination_codec = OggCompressionCodec()

        buffer = BitrateReader.read(filename, source_codec)
        result = BitrateReader.convert(buffer, destination_codec)
        result = AudioMixer().fix(result)

        print(f"[VideoConverter] Conversion finished: {result}")
        return result


# Client Code

if __name__ == "__main__":
    converter = VideoConverter()
    output = converter.convert("funny_cat.ogg", "mp4")
    print(f"[Application] Final Output: {output}")
