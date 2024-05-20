const VKID = window.VKIDSDK;

VKID.Config.set({
    app: 51920522, // App identifier.
    redirectUrl: 'http://localhost/auth', // URL to redirect to after authorization.
});

// Создание экземпляра кнопки.
const oneTap = new VKID.OneTap();

// Получение контейнера из разметки.
const container = document.getElementById('VkIdSdkOneTap');

// Проверка наличия кнопки в разметке.
if (container) {
    // Отрисовка кнопки в контейнере с именем приложения APP_NAME, светлой темой и на русском языке.
    oneTap.render({container: container, scheme: VKID.Scheme.LIGHT, lang: VKID.Languages.RUS});
}