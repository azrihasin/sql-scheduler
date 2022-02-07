let addSubjectBtn = document.querySelector("#add-subject-btn");
let tableForm = document.querySelector(".table-form");
let confirmTableBtn = document.querySelector("#confirm-subject-btn");
let cancelTableBtn = document.querySelector("#cancel-subject-btn");

let closeMenuBtn = document.querySelector("#cancel-subject");
let editSubjectBtn = document.querySelector("#edit-subject");
let removeSubjectBtn = document.querySelector("#remove-subject");

let tableFormAction = "add";

const numtoday = {
    1: "MONDAY",
    2: "TUESDAY",
    3: "WEDNESDAY",
    4: "THURSDAY",
    5: "FRIDAY",
    6: "SATURDAY",
    7: "SUNDAY",
}

// document.querySelector("#uploadpdf-btn").addEventListener('click', (e)=>{
//     const pdf = document.querySelector("#pdfcrs").files[0];
//     const url = 'http://127.0.0.1:5000/table/upload';
//     console.log(pdf);
//     fetchfile(url, pdf, (data)=>{
//         //update table content
//         //build table
//         console.log(data);
//     });
// });

addSubjectBtn.addEventListener('click', (e) => {
    document.querySelector("#day-input").style.display = "inline-block";
    tableForm.style.display = "block";
    tableFormAction = "add";
    document.querySelector("#subject-name").value = "";
    document.querySelector("#start-time").value = "";
    document.querySelector("#end-time").value = "";
});

confirmTableBtn.addEventListener('click', (e) => {
    tableForm.style.display = "none";
    let subject = document.querySelector("#subject-name").value;
    let startTime = document.querySelector("#start-time").value;
    let endTime = document.querySelector("#end-time").value;
    let color = document.querySelector("#color-picker").value;
    console.log(color);
    let days = [];
    for (let item of document.querySelectorAll(".day-input")) {
        if (item.checked) {
            days.push(item.value);
        }
    }
    if(tableFormAction === "add"){
        for (let day of days) {
            addSubject(day, subject, startTime, endTime, color);
        }
    } else{
        console.log("edit subject form");
        updateSubject(subject, startTime, endTime, color);
    }
    updateId();
    buildTable();
});

cancelTableBtn.addEventListener('click', (e) => {
    tableForm.style.display = "none";
    console.log("cancel button");
});

function addSubject(day, subject, startTime, endTime, color) {
    tableContent.push({
        day: parseInt(day),
        subject: subject,
        starttime: startTime.replace(':', ""),
        endtime: endTime.replace(':', ""),
        id: "0",
        color: color,
    });
    updateId();
    console.log(tableContent);
    const url = 'http://127.0.0.1:5000/table/add';
    const data = {
        matricno: userinfo.matricno,
        day: numtoday[day],
        coursecode: subject,
        starttime: startTime.replace(':', ""),
        endtime: endTime.replace(':', "")
    };
    if(isLoggedIn){
        fetchdata(url, data, (responsedata)=>{
            console.log(responsedata);
        });
    }
}

function updateSubject(subject, startTime, endTime, color) {
    let data = {
        matricno: userinfo.matricno,
        day: "0",
        oldsubject: "0",
        newsubject: subject,
        oldstarttime: "0",
        newstarttime: startTime.replace(':', ""),
        endtime: endTime.replace(":", "")
    };
    for(let i = 0 ; i<tableContent.length ; i++){
        if(tableContent[i].id === clickedSubject){
            data.day = numtoday[tableContent[i].day];
            data.oldsubject = tableContent[i].subject;
            data.oldstarttime = tableContent[i].starttime;
            tableContent[i].subject = subject;
            tableContent[i].starttime = startTime.replace(':', "");
            tableContent[i].endtime = endTime.replace(':', "");
            //break;
        }
        if(tableContent[i].subject == subject){
            tableContent[i].color = color;
        }
    }
    const url = 'http://127.0.0.1:5000/table/update';
    if(isLoggedIn){
        fetchdata(url, data, (responsedata)=>{
            console.log(responsedata);
        });
    }
}

function deleteSubject() {
    //todo
}

editSubjectBtn.addEventListener('click', (e)=>{
    console.log(`edit subject ${clickedSubject}`);
    menu.style.display = "none";
    document.querySelector("#day-input").style.display = "none";
    tableForm.style.display = "block";
    tableFormAction = "update";
    for(let i = 0 ; i<tableContent.length ; i++){
        if(tableContent[i].id === clickedSubject){
            document.querySelector("#subject-name").value = tableContent[i].subject;
            document.querySelector("#start-time").value = tableContent[i].starttime.substr(0, 2) + ":" + tableContent[i].starttime.substr(2, 2);
            document.querySelector("#end-time").value = tableContent[i].endtime.substr(0, 2) + ":" + tableContent[i].endtime.substr(2, 2);
            document.querySelector("#color-picker").value = tableContent[i].color;
        }
    }
});

removeSubjectBtn.addEventListener('click', (e)=>{
    console.log(`remove subject ${clickedSubject}`);
    menu.style.display = "none";
    let data = {
        matricno: userinfo.matricno,
        subject: "0",
        day: "0",
        starttime: "0"
    };
    for(let i = 0 ; i<tableContent.length ; i++){
        if(tableContent[i].id === clickedSubject){
            data.subject = tableContent[i].subject;
            data.day = numtoday[tableContent[i].day];
            data.starttime = tableContent[i].starttime;
            tableContent.splice(i, 1);
        }
    }
    const url = "http://127.0.0.1:5000/table/delete";
    if(isLoggedIn){
        fetchdata(url, data, (responsedata)=>{
            console.log(responsedata);
        });
    }
    updateId();
    buildTable();
});

closeMenuBtn.addEventListener('click', (e)=>{
    menu.style.display = "none";
});

buildTable();