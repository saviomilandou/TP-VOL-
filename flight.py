
class Flight:
    def __init__(self, src_code: str, dst_code: str, duration: float):

        self.src_code = src_code
        self.dst_code = dst_code
        self.duration = duration

    #  def info(self): str en boucle
    #    print(f"Bonjour, le code de l'aéroport source {self.src_code} code de l'aéroport destination{self.dst_code} durée du vol {self.duration}.")
