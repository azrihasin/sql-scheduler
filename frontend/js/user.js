let loginBtn = document.querySelector("#login-btn");
let logoutBtn = document.querySelector("#logout-btn");
let loginForm = document.querySelector(".login-form");
let confirmLoginBtn = document.querySelector("#confirm-login-btn");
let cancelLoginBtn = document.querySelector("#cancel-login-btn");

let deleteAccountBtn = document.querySelector("#delete-account-btn");

let profileBtn = document.querySelector("#profile-btn");
let profileView = document.querySelector(".profile-view");
let closeProfileBtn = document.querySelector("#close-profile-btn");
let editProfileBtn = document.querySelector("#edit-profile-btn");
let confirmEditProfileBtn = document.querySelector("#confirm-edit-profile-btn");
let cancelEditProfileBtn = document.querySelector("#cancel-edit-profile-btn");

let registerBtn = document.querySelector(".register-btn");
let registerForm = document.querySelector(".register-form");
let confirmRegisterBtn = document.querySelector("#confirm-register-btn");
let cancelRegisterBtn = document.querySelector("#cancel-register-btn");

let userinfo = {
    isVerified: false,
    studentname: "studentname",
    email: "email",
    kulliyyah: "kulliyyah",
    matricno: "matricno"
};

const daytonum = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 7,
    'MONDAY': 1,
    'TUESDAY': 2,
    'WEDNESDAY': 3,
    'THURSDAY': 4,
    'FRIDAY': 5,
    'SATURDAY': 6,
    'SUNDAY': 7
}


loginBtn.addEventListener('click', (e) => {
    document.querySelector("#login-message").innerHTML = "";
    loginForm.style.display = "block";
    console.log("login");
});

cancelLoginBtn.addEventListener('click', (e) => {
    loginForm.style.display = "none";
});

logoutBtn.addEventListener('click', (e) => {
    loginBtn.style.display = "block";
    logoutBtn.style.display = "none";
    profileBtn.style.display = "none";
    isLoggedIn = false;
    tableContent.splice(0, tableContent.length);
    buildTable();
});

registerBtn.addEventListener('click', (e) => {
    registerForm.style.display = "block";
    loginForm.style.display = "none";
});

cancelRegisterBtn.addEventListener('click', (e) => {
    registerForm.style.display = "none";
});

closeProfileBtn.addEventListener('click', (e) => {
    profileView.style.display = "none";
    document.querySelector(".view-profile").style.display = "block";
});

editProfileBtn.addEventListener('click', (e) => {
    document.querySelector(".view-profile").style.display = "none";
    document.querySelector(".edit-profile").style.display = "block";
});

cancelEditProfileBtn.addEventListener('click', (e) => {
    profileView.style.display = "none";
    document.querySelector(".view-profile").style.display = "none";
    document.querySelector(".edit-profile").style.display = "none";
});

confirmLoginBtn.addEventListener('click', (e) => {
    const email = document.querySelector("#email-login");
    const password = document.querySelector("#password-login");
    const isValid = (email.value.length > 0 && password.value.length > 0);

    if (isValid) {
        verifyUser(email.value, password.value);
    }
    else {
        document.querySelector("#login-message").innerHTML = "Please fill in email and password";
    }
});

confirmRegisterBtn.addEventListener('click', (e) => {
    const studentname = document.querySelector("#username-register").value;
    const email = document.querySelector("#email-register").value;
    const password = document.querySelector("#password-register").value;
    const kulliyyah = document.querySelector("#kulliyyah-register").value;
    const matricno = document.querySelector("#matricno-register").value;
    const isValid = (studentname.length > 0 &&
        email.length > 0 &&
        password.length > 0 &&
        kulliyyah.length > 0 &&
        matricno.length > 0);

    if (isValid) {
        registerForm.style.display = "none";
        registerUser(studentname, email, password, kulliyyah, matricno);
        loginBtn.style.display = "none";
        logoutBtn.style.display = "inline-block";
        profileBtn.style.display = "inline-block";
    } else {
        document.querySelector("#register-message").innerHTML = "Please fill in all the information";
    }
});

deleteAccountBtn.addEventListener('click', (e) => {
    profileView.style.display = "none";
    loginBtn.style.display = "block";
    logoutBtn.style.display = "none";
    profileBtn.style.display = "none";
    isLoggedIn = false;
    tableContent.splice(0, tableContent.length);
    buildTable();
    deleteUser();
});

profileBtn.addEventListener('click', (e) => {
    profileView.style.display = "block";
    document.querySelector(".view-profile").style.display = "block";

    document.querySelector("#username-view").innerHTML = userinfo.studentname;
    document.querySelector("#email-view").innerHTML = userinfo.email;
    document.querySelector("#kulliyyah-view").innerHTML = userinfo.kulliyyah;
    document.querySelector("#matricno-view").innerHTML = userinfo.matricno;
});

confirmEditProfileBtn.addEventListener('click', (e) => {
    profileView.style.display = "none";
    document.querySelector(".view-profile").style.display = "none";
    document.querySelector(".edit-profile").style.display = "none";
    const studentname = document.querySelector("#username-edit").value;
    const email = document.querySelector("#email-edit").value;
    const password = document.querySelector("#password-edit").value;
    const kulliyyah = document.querySelector("#kulliyyah-edit").value;
    const matricno = document.querySelector("#matricno-edit").value;
    console.log(studentname, email, password, kulliyyah, matricno);
    updateUser(studentname, email, password, kulliyyah, matricno);
});

function verifyUser(email, password) {
    const url = 'http://127.0.0.1:5000/user/login';
    let data = {
        email: email,
        password: password
    };
    fetchdata(url, data,
        function (data) {
            if (data[0] === "not found") {
                userinfo.isVerified = false;
                // email.value = "";
                // password.value = "";
                document.querySelector("#login-message").innerHTML = "Wrong password or email";
            } else {
                userinfo.isVerified = true;
                isLoggedIn = true;
                loginForm.style.display = "none";
                loginBtn.style.display = "none";
                logoutBtn.style.display = "inline-block";
                profileBtn.style.display = "inline-block";
                tableContent.splice(0, tableContent.length);
                updateUserInfo(data.studentinfo);
                console.log(data);
                if(data.schedule === "not found"){
                    console.log("no table found");
                }
                else{
                    for (let t of data.schedule) {
                        tableContent.push({
                            day: daytonum[t.day],
                            subject: t.subjectname,
                            starttime: t.starttime,
                            endtime: t.endtime,
                            id: "s0",
                            color: "yellow",
                        });
                    }
                    updateId();
                    buildTable();
                }
            }
        });
}

function updateUserInfo(data) {
    console.log(data);
    userinfo.studentname = data.studentname;
    userinfo.email = data.email;
    userinfo.kulliyyah = data.kulliyyah;
    userinfo.matricno = data.matricno;
}

function registerUser(studentname, email, password, kulliyyah, matricno) {
    const url = 'http://127.0.0.1:5000/user/register';
    let data = {
        matricno: matricno,
        studentname: studentname,
        email: email,
        password: password,
        kulliyyah, kulliyyah
    };
    fetchdata(url, data, function (data) {
        updateUserInfo(data);
        tableContent.splice(0, tableContent.length);
    });
}

function updateUser(studentname, email, password, kulliyyah, matricno) {
    const url = 'http://127.0.0.1:5000/user/update';
    data = {
        matricno: userinfo.matricno,
        newmatricno: matricno,
        studentname: studentname,
        email: email,
        password, password,
        kulliyyah, kulliyyah
    };
    console.log(data);
    fetchdata(url, data, function (responsedata) {
        console.log(responsedata);
        updateUserInfo({
            studentname: studentname,
            email: email,
            kulliyyah: kulliyyah,
            matricno: matricno
        });
    });
}

function deleteUser() {
    const url = 'http://127.0.0.1:5000/user/delete';
    data = { matricno: userinfo.matricno };
    fetchdata(url, data, function (data) {
        console.log(data);
    });
}