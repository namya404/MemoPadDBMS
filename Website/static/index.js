function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

// function editNote(noteId) {
//   fetch("/edit-note", {
//     method: "POST",
//     body: JSON.stringify({ noteId: noteId }),
//   }).then((_res) => {
//     window.location.href = "/";
//   });
// }