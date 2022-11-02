from observador import NotificadorEmail, NotificadorMensagem, NotificadorPushNotification
from social_media import Perfil


# Cliente
if __name__ == "__main__":
    seguidores_mensagem = ["Carlos", "Claudia", "Marcia", "Rodolfo"]
    seguidores_push_notification = ["Carlos"]
    seguidores_email = ["Claudia", "Marcia"]

    meu_perfil = Perfil()
    NotificadorMensagem(meu_perfil, seguidores_mensagem)
    NotificadorPushNotification(meu_perfil, seguidores_push_notification)
    NotificadorEmail(meu_perfil, seguidores_email)

    meu_perfil.adicionar_post("Ola universo da Programacao!")