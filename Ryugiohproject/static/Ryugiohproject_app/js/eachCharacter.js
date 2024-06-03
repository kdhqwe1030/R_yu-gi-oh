document.addEventListener('DOMContentLoaded', function() {
    const urlParams = new URLSearchParams(window.location.search);
    const character = urlParams.get('character');
    
    if (character) {
        fetchCharacterDeck(character, 'effect', '#effect-cards .container');
        fetchCharacterDeck(character, 'normal', '#normal-cards .container');
        fetchCharacterDeck(character, 'spell', '#spell-cards .container');
        fetchCharacterDeck(character, 'trap', '#trap-cards .container');
    }

    function fetchCharacterDeck(character, frameType, containerSelector) {
        fetch(`/api/character-deck/${frameType}/?character=${character}`)
            .then(response => response.json())
            .then(data => {
                const container = document.querySelector(containerSelector);
                data.forEach(card => {
                    const cardElement = document.createElement('div');
                    cardElement.className = 'card';
                    cardElement.style.backgroundImage = `url(${card.card_images[0].image_url})`;
                    container.appendChild(cardElement);
                });
            })
            .catch(error => console.error('Error fetching card data:', error));
    }
});
