import { books, init_zoom } from "./buffer.js";


const bookList = document.querySelector('.book-list');
const sortSelect = document.querySelector('#sort-select');


function displayBooks() {
  const bookList = document.querySelector('#book-list');
  bookList.innerHTML = '';
  books.forEach(book => {
    const book_el = document.createElement('div');
    const bookURL = `book_detail/?id=${book.id}`
    book_el.classList.add('book');
    book_el.innerHTML = `
      <img src="${book.image}" alt="${book.title}">
      <div class="book-info">
        <h3>${book.genre}</h3>
        <p>${book.author}</p>
        <a href="${bookURL}" target="_blank" class="details-link">more...</a>
      </div>
      `;

      bookList.appendChild(book_el);
  });
  init_zoom('book');
}

// Function to sort books by author
function sortByAuthor() {
  const booksCopy = [...books];
  const sortedBooks = booksCopy.sort((a, b) => a.author.localeCompare(b.author));
  bookList.innerHTML = '';
  sortedBooks.forEach(book => {
    const bookElement = document.createElement('div');
    const bookURL = `book_detail/?id=${book.id}`
    bookElement.classList.add('book');
    bookElement.innerHTML = `
    <img src="${book.image}" alt="${book.title}">
    <div class="book-info">
      <h3>${book.genre}</h3>
      <p>${book.author}</p>
      <a href="${bookURL}" target="_blank" class="details-link">more...</a>
    </div>
    `;
      bookList.appendChild(bookElement);
    });
    init_zoom('book');
  }

// Function to sort books by genre
function sortByGenre() {
  const booksCopy = [...books];
  const sortedBooks = booksCopy.sort((a, b) => a.genre.localeCompare(b.genre));
  bookList.innerHTML = '';
  sortedBooks.forEach(book => {
    const bookElement = document.createElement('div');
    const bookURL = `book_detail/?id=${book.id}`
    bookElement.classList.add('book');
    bookElement.innerHTML = `
    <img src="${book.image}" alt="${book.title}">
    <div class="book-info">
      <h3>${book.genre}</h3>
      <p>${book.author}</p>
      <a href="${bookURL}" target="_blank" class="details-link">more...</a>
    </div>
    `;
    bookList.appendChild(bookElement);
  });
  init_zoom('book');
}



// Event listener to sort books when the user selects an option from the dropdown
sortSelect.addEventListener('change', (event) => {
  if (event.target.value === 'author') {
    sortByAuthor();
  } else if (event.target.value === 'genre') {
    sortByGenre();
  }
});


// Generate the book list on page load
displayBooks();

