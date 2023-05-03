import { books, init_zoom } from "./buffer.js";

// Get the book ID from the URL query string
const urlParams = new URLSearchParams(window.location.search);
const bookId = urlParams.get('id');

// Find the book with the matching ID
const book = books.find(book => book.id === Number(bookId));

// Update the DOM with the book details
const webTitle = document.getElementById('webTitle')
const bookCover = document.getElementById('book-cover');
const bookTitle = document.getElementById('book-title');
const bookAuthor = document.getElementById('book-author');
const bookGenre = document.getElementById('book-genre');
const bookDescription = document.getElementById('book-description');
const bookCharacteristics = document.getElementById('book-characteristics');

webTitle.innerText = `Libra.IO / ${book.title}`
bookCover.src = '../' + book.image;
bookTitle.innerText = book.title;
bookAuthor.innerText = `Author: ${book.author}`;
bookGenre.innerText = `Genre: ${book.genre}`;
bookDescription.innerText = book.description;
bookCharacteristics.innerText = book.characteristics;

init_zoom('book-detail');
