<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>삼둘푸드</title>
</head>
<body>
    <h1>음식 이름 입력</h1>
    <form id="foodForm">
        <label for="foodName">음식 이름: </label>
        <input type="text" id="foodName" name="foodName" required>
        <button type="submit">저장</button>
    </form>

    <script>
        document.getElementById("foodForm").addEventListener("submit", function(event) {
            event.preventDefault(); // 폼 기본 제출 방지

            const foodName = document.getElementById("foodName").value;
            const url = `http://ec2-43-203-204-195.ap-northeast-2.compute.amazonaws.com/n03/food?name=${encodeURIComponent(foodName)}`;

            fetch(url, {
                method: 'GET',
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    </script>
    <script>
	// Import the functions you need from the SDKs you need
	import { initializeApp } from "firebase/app";
	import { getAnalytics } from "firebase/analytics";
	// TODO: Add SDKs for Firebase products that you want to use
	// https://firebase.google.com/docs/web/setup#available-libraries

	// Your web app's Firebase configuration
	// For Firebase JS SDK v7.20.0 and later, measurementId is optional
	const firebaseConfig = {
  		apiKey: "AIzaSyDLkLiyBsrltR9nrqaLv5Ic6pAtlOneaqo",
  		authDomain: "samdul03food-83d92.firebaseapp.com",
  		projectId: "samdul03food-83d92",
  		storageBucket: "samdul03food-83d92.appspot.com",
  		messagingSenderId: "442399641270",
  		appId: "1:442399641270:web:46015a27d5c246c3dfe017",
 		 measurementId: "G-3HGH7FX7JH"
	};

	// Initialize Firebase
	const app = initializeApp(firebaseConfig);
	const analytics = getAnalytics(app);
	</script>
</body>
</html>
