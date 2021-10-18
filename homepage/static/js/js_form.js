function search() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  tr = table.getElementsByTagName("tr");
  if (table == document.getElementById("store")) {
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
}

function trigger() {
  functions = document.querySelector("#ferranMessage:checked");
  td = tr[i].getElementsByTagName("td")[3];
  if (td && functions.checked) {
    txtValue = td.textContent || td.innerText;
    console.log(txtValue);
    if (txtValue == "1") {
      document.getElementById("mycheckbox1").checked = true;
      document.getElementById("mycheckbox2").checked = true;
      document.getElementById("mycheckbox3").checked = true;
      document.getElementById("mycheckbox4").checked = true;
      document.getElementById("mycheckbox5").checked = true;
      document.getElementById("mycheckbox6").checked = true;
    }
  }
}
