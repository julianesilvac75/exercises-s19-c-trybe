from observador import NotificadorEmail, NotificadorMensagem, NotificadorPushNotification
from social_media import Perfil


# Cliente
if __name__ == "__main__":
    seguidores_mensagem = ["Carlos", "Claudia", "Marcia", "Rodolfo"]
    seguidores_push_notification = ["Carlos"]
    seguidores_email = ["Claudia", "Marcia"]

    meu_perfil = Perfil()
    notificador_mensagem = NotificadorMensagem(meu_perfil, seguidores_mensagem)
    notificador_push_notification = NotificadorPushNotification(meu_perfil, seguidores_push_notification)
    notificador_email = NotificadorEmail(meu_perfil, seguidores_email)

    meu_perfil.adicionar_post("Ola universo da Programacao!")

    meu_perfil.remover_sistema_de_notificacao(notificador_email)
    meu_perfil.adicionar_post("Esse eh o post sem email")

    meu_perfil.adicionar_sistema_de_notificacao(notificador_email)
    meu_perfil.adicionar_post("Esse eh o post com todos")

    meu_perfil.remover_sistema_de_notificacao(notificador_push_notification)
    meu_perfil.adicionar_post("Esse eh o post sem push notification")

