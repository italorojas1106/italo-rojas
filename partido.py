class Match:
    def __init__(self, match_data, equipos, estadios):
        self.id = match_data['id']
        self.number = match_data['number']
        self.home = self.get_equipo_by_id(match_data['home']['id'], equipos)
        self.away = self.get_equipo_by_id(match_data['away']['id'], equipos)
        self.date = match_data['date']
        self.group = match_data['group']
        self.estadio = self.get_estadio_by_id(match_data['stadium_id'], estadios)

    def get_equipo_by_id(self, equipo_id, equipos):
        for equipo in equipos:
            if equipo.id == equipo_id:
                return equipo
        return None

    def get_estadio_by_id(self, estadio_id, estadios):
        for estadio in estadios:
            if estadio.id == estadio_id:
                return estadio
        return None