// 🌿 Handle drag-and-drop upload and preview

const uploadBox = document.getElementById('uploadBox');
const imageInput = document.getElementById('imageInput');
const preview = document.getElementById('preview');
const previewImage = document.getElementById('previewImage');

// Click to open file dialog
uploadBox.addEventListener('click', () => imageInput.click());

// Show preview when a file is selected
imageInput.addEventListener('change', () => {
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = e => {
            previewImage.src = e.target.result;
            preview.classList.remove('hidden');
        };
        reader.readAsDataURL(file);
    }
});

// Drag and drop styling
uploadBox.addEventListener('dragover', e => {
    e.preventDefault();
    uploadBox.style.background = '#e8f5e9';
});

uploadBox.addEventListener('dragleave', e => {
    e.preventDefault();
    uploadBox.style.background = '#f9fff9';
});

uploadBox.addEventListener('drop', e => {
    e.preventDefault();
    uploadBox.style.background = '#f9fff9';
    const file = e.dataTransfer.files[0];
    imageInput.files = e.dataTransfer.files;

    const reader = new FileReader();
    reader.onload = event => {
        previewImage.src = event.target.result;
        preview.classList.remove('hidden');
    };
    reader.readAsDataURL(file);
});
