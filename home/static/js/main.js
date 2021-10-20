// $(document).ready(function() {
// 	$('.ui.basic').click(() => {
// 		console.log('aaaaa')
// 			.sidebar('toggle')
// 	});
// });

//Function_of_User
function Search() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("searchArticles");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[2];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

//Role login
function onToggle() {
  var rowId = event.target.parentNode.parentNode.id;
  console.log(rowId);
  var data = document.getElementById(rowId).querySelectorAll("#function_U");
  var tokenAmount = document.getElementById(rowId).querySelectorAll(".btn");
  var role = document
    .getElementById(rowId)
    .querySelectorAll(".table-head")[0].id;
  console.log(role);
  var doc2 = document.getElementById(rowId).querySelectorAll("#mycheckbox1")[0];
  console.log(doc2);
  var doc3 = document.getElementById(rowId).querySelectorAll("#mycheckbox2")[0];
  console.log(doc3);
  var doc4 = document.getElementById(rowId).querySelectorAll("#mycheckbox3")[0];
  console.log(doc4);
  var doc5 = document.getElementById(rowId).querySelectorAll("#mycheckbox4")[0];
  console.log(doc5);
  var doc6 = document.getElementById(rowId).querySelectorAll("#mycheckbox5")[0];
  console.log(doc6);
  var doc7 = document.getElementById(rowId).querySelectorAll("#mycheckbox6")[0];
  console.log(doc7);
  var doc1 = document.getElementById("mycheckbox1");
  console.log(doc1);
  tokenAmount = data[0].innerHTML;
  if (
    doc2.checked == true ||
    doc3.checked == true ||
    doc4.checked == true ||
    doc5.checked == true ||
    doc6.checked == true ||
    doc7.checked == true
  ) {
    doc2.checked = false;
    doc3.checked = false;
    doc4.checked = false;
    doc5.checked = false;
    doc6.checked = false;
    doc7.checked = false;
  } else if (tokenAmount == 1) {
    // if checked

    doc2.checked = true;
    doc3.checked = true;
    doc4.checked = true;
    doc5.checked = true;
    doc6.checked = true;
    doc7.checked = true;
  } else if (tokenAmount == 2) {
    doc2.checked = true;
    doc3.checked = false;
    doc4.checked = false;
    doc5.checked = false;
    doc6.checked = false;
    doc7.checked = false;
  } else if (tokenAmount == 3) {
    doc2.checked = false;
    doc3.checked = true;
    doc4.checked = false;
    doc5.checked = false;
    doc6.checked = false;
    doc7.checked = false;
  } else if (tokenAmount == 4) {
    doc2.checked = false;
    doc3.checked = false;
    doc4.checked = true;
    doc5.checked = false;
    doc6.checked = false;
    doc7.checked = false;
  } else if (tokenAmount == 5) {
    doc2.checked = false;
    doc3.checked = false;
    doc4.checked = false;
    doc5.checked = true;
    doc6.checked = false;
    doc7.checked = false;
  } else if (tokenAmount == 6) {
    doc2.checked = false;
    doc3.checked = false;
    doc4.checked = false;
    doc5.checked = false;
    doc6.checked = true;
    doc7.checked = false;
  } else if (tokenAmount == 7) {
    doc2.checked = false;
    doc3.checked = false;
    doc4.checked = false;
    doc5.checked = false;
    doc6.checked = false;
    doc7.checked = true;
  } else if (tokenAmount == 0 || tokenAmount == null) {
    // if unchecked

    doc2.checked = false;
    doc3.checked = false;
    doc4.checked = false;
    doc5.checked = false;
    doc6.checked = false;
    doc7.checked = false;
  }
}

function htmlbodyHeightUpdate() {
  var height3 = $(window).height();
  var height1 = $(".nav").height() + 50;
  height2 = $(".main").height();
  if (height2 > height3) {
    $("html").height(Math.max(height1, height3, height2) + 10);
    $("body").height(Math.max(height1, height3, height2) + 10);
  } else {
    $("html").height(Math.max(height1, height3, height2));
    $("body").height(Math.max(height1, height3, height2));
  }
}
$(document).ready(function () {
  htmlbodyHeightUpdate();
  $(window).resize(function () {
    htmlbodyHeightUpdate();
  });
  $(window).scroll(function () {
    height2 = $(".main").height();
    htmlbodyHeightUpdate();
  });
});

//active_user
function active_user() {
  var rowId = event.target.parentNode.parentNode.id;
  console.log(rowId);
  var data = document.getElementById(rowId).querySelectorAll(".badge")[0];
  console.log(data);
  var text = document
    .getElementById(rowId)
    .querySelectorAll("#active_U").className;
  console.log(text);
  var tokenAmount = document
    .getElementById(rowId)
    .querySelectorAll(".btn-info");
  console.log(tokenAmount);
  var status = document.getElementById(rowId).querySelectorAll(".btn-info")[0];
  console.log(status);
  // var role = document.getElementById(rowId).querySelectorAll(".badge");
  // console.log(role);
  tokenAmount = data.innerHTML;
  console.log(tokenAmount);
  if (tokenAmount == "Active") {
    status.style.background = "gray";
  } else {
    data.setText("Active");
    console.log(data);
  }
}
