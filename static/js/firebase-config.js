// For Firebase JS SDK v7.20.0 and later, measurementId is optional


import { initializeApp } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js";
import {
    getAuth,
    GoogleAuthProvider
} from "https://www.gstatic.com/firebasejs/10.9.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.9.0/firebase-firestore.js";

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyDcP9mf_SIIAX-npj8CFuSXjVDvOoh2MSQ",
    authDomain: "jbk-flask-website-e7499.firebaseapp.com",
    projectId: "jbk-flask-website-e7499",
    storageBucket: "jbk-flask-website-e7499.firebasestorage.app",
    messagingSenderId: "262510545759",
    appId: "1:262510545759:web:ceb19d96b029a1059684ea",
    measurementId: "G-FT9SRS5H5H"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();

const db = getFirestore(app);

export { auth, provider, db };