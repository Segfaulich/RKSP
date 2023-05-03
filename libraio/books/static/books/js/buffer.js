export {};

const books = [
    {
        id: 1,
        title: "War & Peace",
        author: "Lev Tolstoy",
        genre: "Novel",
        price: 10.99,
        image: "../img/warnpeace.jpeg",
  
        description: "The story describes a number of important historical events and the realities of society. The epic novel touches on many important themes: friendship, love, duty, and others. At the same time, the whole story is permeated by the confrontation of war and peace, not only in a global sense, but also in the mental changes of each hero.",
        characteristics: [
          "Published: 1960",
          "Pages: 281",
          "Language: English",
          "Publisher: J. B. Lippincott & Co."
        ]
    },
    {
        id: 2,
        title: "Murder on the Orient Express",
        author: "Agatha Christie",
        genre: "Detective Stories",
        price: 12.99,
        image: "../img/murderinthesttrain.jpeg",
  
        description: "A trip on one of Europe's most luxurious trains unexpectedly turns into one of the most stylish and fascinating mysteries in history. The film tells the story of thirteen train passengers, all of whom are under suspicion. And only the detective must solve the puzzle as quickly as possible before the criminal strikes again.",
        characteristics: [
          "Published: 1960",
          "Pages: 281",
          "Language: English",
          "Publisher: J. B. Lippincott & Co."
        ]
    },
    {   id: 3,
        title: "Beach Murder",
        author: "Chris Chibnall",
        genre: "Prose",
        price: 8.99,
        image: "../img/murderonthebeach.jpeg",
  
        description: "In a small town, eleven-year-old Danny disappears. A day later his body was found by the sea... Detectives Alec Hardy and Ellie Miller are determined to find the killer. One by one, the good citizens fall under suspicion, including the vicar, the store owner and even the boy's father! It turns out that each of them has a skeleton in the closet. But when the mystery stops being a mystery, the town shudders...",
        characteristics: [
          "Published: 1960",
          "Pages: 281",
          "Language: English",
          "Publisher: J. B. Lippincott & Co."
        ]
    },
    {   id: 4,
        title: "Crime and Punishment",
        author: "Fedor Dostoevsky",
        genre: "Novel",
        price: 11.99,
        image: "../img/crimeandpunishment.jpeg",
  
        description: "Fyodor Mikhailovich Dostoyevsky's novel Crime and Punishment was written in 1866. The idea for the work came to the writer back in 1859, when he was serving his sentence in the penal colony. Dostoevsky had originally planned to write his novel Crime and Punishment in the form of a confession, but in the process the original idea gradually changed and when describing his new work to the editor of the Russian Gazette (in which the book was first published) the author describes the novel as `a psychological account of one crime`",
        characteristics: [
          "Published: 1960",
          "Pages: 281",
          "Language: English",
          "Publisher: J. B. Lippincott & Co."
        ]
    }
  ];

export function init_zoom(class_name){
  // Get the modal
  const modal = document.getElementById("bookModal");

  // Get the image and book element
  const bookImage = document.getElementById("bookImage");
  const bookElements = document.querySelectorAll('.' + class_name);

  // Add click event listener to each book element
  bookElements.forEach((bookElement) => {
    const bookImg = bookElement.querySelector('img');
    bookImg.addEventListener('click', () => {
      // Set the book image source and display the modal
      bookImage.src = bookImg.src;
      modal.style.display = "block";
    });
  });

  // Add click event listener to close button
  modal.addEventListener('click', () => {
    modal.style.display = "none";
  });

  // Add click event listener to modal content (to close on click outside image)
  modal.addEventListener('click', (event) => {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  });
}

export { books };