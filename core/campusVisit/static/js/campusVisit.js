
document.addEventListener("DOMContentLoaded", function () {
  var currentTag = document.getElementsByClassName("active")
  currentTag[0].classList.remove("active");
  var element = document.getElementById("id_campusVisit");
  element.classList.add('active')
});



// Adding Alumni form script====================================================================

// const addMoreAlumni=document.getElementById('add-more-alumni')
// addMoreAlumni.addEventListener('click',add_alumni_form)

function add_alumni_form(event) {
  if (event) {
    event.preventDefault();
  }

  //Incrementing the total forms count
  const totalForms = document.getElementById('id_Alumni-TOTAL_FORMS')
  let formCount = Number(totalForms.value)

  if (formCount < 5) {
    totalForms.value = formCount + 1;
    alumniCounter = totalForms.value;
    //Creating new form element
    let form = document.querySelectorAll(".alumniForm");
    let alumniFormsCopy = form[0].cloneNode(true);

    //Editing the inner values
    const regex = new RegExp('-0-', 'g');
    alumniFormsCopy.innerHTML = alumniFormsCopy.innerHTML.replace(regex, `-${formCount}-`);

    counterHTML = alumniFormsCopy.querySelector("#Alumni-Counter");
    counterHTML.innerHTML = `Alumni ${alumniCounter}`;

    //Adding constant fields
    alumniFormsCopy.querySelector("#id_Alumni-" + formCount + "-arrivalDate").value = document.getElementById("id_Alumni-0-arrivalDate").value;
    alumniFormsCopy.querySelector("#id_Alumni-" + formCount + "-purposeOfVisit").value = document.getElementById("id_Alumni-0-purposeOfVisit").value;

    //Showing the cross button
    var temp = alumniFormsCopy.querySelector(".close");
    temp.removeAttribute("style");


    //Copying the new form to the target
    const alumniFormCopyTarget = document.getElementById('alumni-Form-List')
    alumniFormCopyTarget.append(alumniFormsCopy)
  } else {

  }

}

// Adding Guest form script====================================================================

const addMoreGuest = document.getElementById('add-more-guest')

function add_guest_form(event) {
  if (event) {
    event.preventDefault()
  }

  //Incrementing the total forms count
  const totalForms = document.getElementById('id_Guest-TOTAL_FORMS')
  let formCount = Number(totalForms.value)

  if (formCount < 5) {
    totalForms.value = formCount + 1
    guestCounter = totalForms.value

    //Creating new form element
    let form = document.querySelectorAll(".guestForm")
    let guestFormsCopy = form[0].cloneNode(true)

    //Editing the inner values
    const regex = new RegExp('-0-', 'g');
    guestFormsCopy.innerHTML = guestFormsCopy.innerHTML.replace(regex, `-${formCount}-`);

    counterHTML = guestFormsCopy.querySelector("#Guest-Counter");
    counterHTML.innerHTML = `Guest ${guestCounter}`

    //Showing the cross button
    var temp = guestFormsCopy.querySelector(".close");
    temp.removeAttribute("style");

    //Copying the new form to the target
    const guestFormsCopyTarget = document.getElementById('guest-Form-List')
    guestFormsCopyTarget.append(guestFormsCopy)
  } else {

  }
}

// Get the non-alumni part element====================================================================
function toggleNonAlumniPart() {
  var nonAlumniPart = document.getElementById('non-alumni-container-1');

  if (nonAlumniPart.style.display === 'block') {

  } else {
    document.getElementById('duelAddBtn').style.display = 'none';
    document.getElementById('singleAddBtn').style.display = 'block';

    nonAlumniPart.style.display = 'block';
  }
}

async function fetchData(mergedForms) {
  const response = await fetch(url1, { method: 'POST', body: mergedForms });
  if (response.ok) {
    window.location.reload();
  } else {
    const data = await response.json();
    return JSON.parse(data.errors);
  }
}


function submit_form(event) {
  event.preventDefault()
  alumniForm = document.getElementById("alumni-information-form");
  guestForm = document.getElementById("guest-information-form");

  var alumniFormData = new FormData(alumniForm);
  var guestFormData = new FormData(guestForm);
  var mergedForms = new FormData();

  alumniFormData.forEach(function (value, key) {
    mergedForms.append(key, value);
  });
  var csrfToken1 = alumniForm.querySelector('input[name="csrfmiddlewaretoken"]');
  mergedForms.append('csrfmiddlewaretoken', csrfToken1.value);

  guestFormData.forEach(function (value, key) {
    mergedForms.append(key, value);
  });
  var csrfToken2 = guestForm.querySelector('input[name="csrfmiddlewaretoken"]');
  mergedForms.append('csrfmiddlewaretoken', csrfToken2.value);



  errorDiv = document.getElementById('errorDiv')

  fetchData(mergedForms).then(data => {
    if (data.errors.length == 0) {
      window.location.reload();
    } else {
      var errBox = document.getElementById("errorBox")
      if (errBox.style.display === 'none') {
        errBox.style.display = 'block';
      }
      var singleError = document.getElementById("individual-error");
      singleError.innerHTML = "";
      data.errors.forEach(error => {
        if (error[0] == 'This field is required.') {
          error[0] = 'All fields are required.';
        }
        singleError.innerHTML = singleError.innerHTML + error[0] + "<br>";
      })
    }
  }).catch(error => {
    console.log(error)
  })
}

function removeAlumniForm(formInput) {
  var idNum = parseInt(formInput.id.toString().split("-")[1]);

  let formList = document.getElementsByClassName("alumniForm");
  var flag = 0;
  var length = formList.length;

  for (var i = 0; i < length; i++) {
    var regexTemp = new RegExp("Alumni-[0-4]-firstName");
    var idForm = parseInt(formList[i].innerHTML.match(regexTemp).toString().split("-")[1]);
    if (flag == 1) {
      var id = "id_Alumni-" + idForm + "-";
      // console.log(id)
      var inputFields = [
        "firstName",
        "lastName",
        "email",
        "phoneNumber",
        "BitsId",
        "purposeOfVisit",
        "arrivalDate",
        "currCompany",
        "CompanyDesignation",
        "currAddress",
        "city",
        "state",
        "country",
        "zip"
      ];

      var valueList = []

      inputFields.forEach(function (fieldName) {
        valueList.push(document.getElementById(id + fieldName).value);
      });

      const regex = new RegExp('-' + idForm + '-', 'g');
      formList[i].innerHTML = formList[i].innerHTML.replace(regex, `-${idForm - 1}-`);

      var idNew = "id_Alumni-" + (idForm - 1) + "-";
      for (var j = 0; j < inputFields.length; j++) {
        document.getElementById(idNew + inputFields[j]).value = valueList[j];
      }


      counterHTML = formList[i].querySelector("#Alumni-Counter");
      counterHTML.innerHTML = `Alumni ${i + 1}`;
    }

    if (idNum == idForm) {
      flag = 1;
      if (i > 0) {
        formList[i].remove();
        const totalForms = document.getElementById('id_Alumni-TOTAL_FORMS')
        totalForms.value = totalForms.value - 1;
        length--;
        i--;
      }
    }
  }
}


function removeGuestForm(formInput) {
  var idNum = parseInt(formInput.id.toString().split("-")[1]);
  let formList = document.getElementsByClassName("guestForm");
  var flag = 0;
  var length = formList.length;

  for (var i = 0; i < length; i++) {
    var regexTemp = new RegExp("Guest-[0-4]-firstName");
    var idForm = parseInt(formList[i].innerHTML.match(regexTemp).toString().split("-")[1]);
    if (flag == 1) {
      var id = "id_Guest-" + idForm + "-";
      var inputFields = [
        "firstName",
        "lastName",
        "email",
        "phoneNumber"
      ];

      var valueList = []

      inputFields.forEach(function (fieldName) {
        valueList.push(document.getElementById(id + fieldName).value);
      });

      const regex = new RegExp('-' + idForm + '-', 'g');
      formList[i].innerHTML = formList[i].innerHTML.replace(regex, `-${idForm - 1}-`);

      var idNew = "id_Guest-" + (idForm - 1) + "-";
      for (var j = 0; j < inputFields.length; j++) {
        document.getElementById(idNew + inputFields[j]).value = valueList[j];
      }


      counterHTML = formList[i].querySelector("#Guest-Counter");
      counterHTML.innerHTML = `Guest ${i + 1}`;
    }

    if (idNum == idForm) {
      flag = 1;
      if (i > 0) {
        formList[i].remove();
        const totalForms = document.getElementById('id_Guest-TOTAL_FORMS')
        totalForms.value = totalForms.value - 1;
        length--;
        i--;
      }
    }
  }
}