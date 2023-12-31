class FilmwebExporter:
    """Class for exporting data from Filmweb."""

    def __init__(self, username):
        self.username = username

    def export(self):
        """Export data from Filmweb."""
        return f"Exporting {self.username} data..."


if __name__ == "__main__":
    exporter = FilmwebExporter("johndoe")
    print(exporter.export())
