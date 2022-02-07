let isLoggedIn = false;
let menu = document.querySelector("#menu");
let clickedSubject = "ss";

let tableContent = [
    // {
    //     day: 1,
    //     subject: 'csc 1200',
    //     starttime: "1100",
    //     endtime: "1250",
    //     id: "s50",
    //     color: "yellow",
    // },
    // {
    //     day: 1,
    //     subject: 'ungs 5000',
    //     starttime: "0900",
    //     endtime: "1010",
    //     id: "s1",
    //     color: "green",
    // },
    // {
    //     day: 2,
    //     subject: 'le 1200',
    //     starttime: "0850",
    //     endtime: "1100",
    //     id: "s2",
    //     color: "blue",
    // },
    // {
    //     day: 2,
    //     subject: 'info 1200',
    //     starttime: "1115",
    //     endtime: "1310",
    //     id: "s3",
    //     color: "yellow",
    // },
    // {
    //     day: 3,
    //     subject: 'info 1200',
    //     starttime: "0900",
    //     endtime: "1050",
    //     id: "s4",
    //     color: "red",
    // },
    // {
    //     day: 3,
    //     subject: 'info 1200',
    //     starttime: "1100",
    //     endtime: "1250",
    //     id: "s5",
    //     color: "red",
    // },
    // {
    //     day: 6,
    //     subject: 'bm',
    //     starttime: "1100",
    //     endtime: "1250",
    //     id: "s6",
    //     color: "green",
    // }
];

function updateId(){
    let index = 0;
    for(let t of tableContent){
        t.id = `s${index}`;
        index++;
    }
}

function addTableHeader(table) {
    table.innerHTML = `
    <div class="table-header">
    <div>#</div>
    <div>Mon</div>
    <div>Tue</div>
    <div>Wed</div>
    <div>Thu</div>
    <div>Fri</div>
    <div>Sat</div>
    <div>Sun</div>
    </div>`;
}

function addTableTime(table) {
    let start = parseInt((tableContent[0].starttime).substr(0, 2));
    let end = parseInt((tableContent[0].endtime).substr(0, 2));
    for (let t of tableContent) {
        if (parseInt((t.starttime).substr(0, 2)) < start) start = parseInt((t.starttime).substr(0, 2));
        if (parseInt((t.endtime).substr(0, 2)) > end) end = (parseInt((t.endtime).substr(0, 2)) + 1);
    }
    const rownum = (end - start) + 1;
    //console.log(start, end);
    for (let i = start; i < (start + rownum); i++) {
        table.innerHTML += `<div
            style="grid-row: ${((i - start) * 60) + 2}/${((i - start) * 60) + 62}; 
            grid-col: 1/2; height: 60px;">
            ${i < 13 ? i % 13 : (i % 13) + 1}:00 ${i < 12 ? 'am' : 'pm'}
        </div>`;
    }
}

function buildTable() {
    const table = document.querySelector(".table");
    addTableHeader(table);
    if(tableContent.length < 1){
        table.innerHTML += "<div>Your schedule is empty!!!</div>"
        return;
    }
    addTableTime(table);
    let start = parseInt((tableContent[0].starttime).substr(0, 2));
    let end = parseInt((tableContent[0].endtime).substr(0, 2));
    for (let t of tableContent) {
        if (parseInt((t.starttime).substr(0, 2)) < start) start = parseInt((t.starttime).substr(0, 2));
        if (parseInt((t.endtime).substr(0, 2)) > end) end = (parseInt((t.endtime).substr(0, 2)) + 1);
    }
    const rownum = (end - start) + 1;
    for (let t of tableContent) {
        table.innerHTML += `<div class="${t.subject.replace(/\s+/g, '')} subject" id="${t.id}">${t.subject}</div>`;
        const item = document.querySelector(`#${t.id}`);
        item.style.backgroundColor = t.color;
        item.style.gridColumn = `${t.day + 1}/${t.day + 2}`;
        const starttime = (parseInt(t.starttime.substr(0, 2)) * 60) + parseInt(t.starttime.substr(2, 2));
        const endtime = (parseInt(t.endtime.substr(0, 2)) * 60) + parseInt(t.endtime.substr(2, 2));
        console.log(starttime, endtime);
        item.style.gridRow = `${starttime - (start * 60) + 2}/${endtime - (start * 60) + 2}`;
    }
    for (let t of tableContent) {
        document.querySelector(`#${t.id}`).addEventListener('click', (e) => {
            showmenu(e.target.id);
        });
    }
}

function showmenu(id) {
    console.log(`${id} clicked`);
    clickedSubject = id;
    menu.style.display = "block";
    const clicked = document.querySelector(`#${id}`);
    const top = clicked.offsetTop-50;
    const left = clicked.offsetLeft;
    console.log(clicked.offsetTop);
    menu.style.top = `${top}px`;
    menu.style.left = `${left}px`;
}