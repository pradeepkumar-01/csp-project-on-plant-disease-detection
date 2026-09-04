function showPlant(plantName) {
    document.querySelectorAll('.plant-info').forEach(section => section.classList.add('hidden'));
    document.getElementById(plantName).classList.remove('hidden');
    window.scrollTo({ top: 400, behavior: 'smooth' });
}
