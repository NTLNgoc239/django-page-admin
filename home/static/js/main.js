// $(document).ready(function() {
// 	$('.ui.basic').click(() => {
// 		console.log('aaaaa')
// 			.sidebar('toggle')
// 	});
// });
function search() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
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
function onToggle() {
  var rowId = event.target.parentNode.parentNode.id;
  // console.log(rowId);
  // console.log(typeof "rowId");
  //this gives id of tr whose button was clicked
  var data = document.getElementById(rowId).querySelectorAll("#function_U");
  // console.log(data);
  var tokenAmount = document.getElementById(rowId).querySelectorAll(".btn");
  // console.log(tokenAmount);
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
  // var checkbox1 = document
  //   .getElementById(rowId)
  //   .querySelectorAll("#mycheckbox1{{i}}");
  // console.log(checkbox1);
  var doc1 = document.getElementById("mycheckbox1");
  console.log(doc1);
  tokenAmount = data[0].innerHTML;
  // console.log(tokenAmount);
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
