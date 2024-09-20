let currentImageIndex = 0; // Índice actual de la imagen

// Obtener las URLs de las imágenes desde el HTML
const imageElements = document.querySelectorAll('#image-urls span');
const imageUrls = Array.from(imageElements).map(element => element.getAttribute('data-url'));



function changeImage(direction) {
    currentImageIndex += direction;

    if (currentImageIndex < 0) {
        currentImageIndex = imageUrls.length - 1; // Volver al final si el índice es menor que 0
    } else if (currentImageIndex >= imageUrls.length) {
        currentImageIndex = 0; // Volver al inicio si el índice es mayor que la cantidad de imágenes
    }

    // Cambiar la imagen principal
    document.getElementById("main-image").src = imageUrls[currentImageIndex];
}