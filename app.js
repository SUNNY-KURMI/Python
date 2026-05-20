function Calfactorial(n){
    if( n < 0){
        return "factorial is not define for negative number.";
    } else if (n === 0 || n === 1){
        return 1;
    } else {
        let result = 1;
        for (let i=2;i<=n;i++){
            result = result*i;
        }
         return result ;
    }
}

const userinput = prompt("Enter a non-negative number: ");
const number = parseInt(userinput);

const resultElement = document.getElementById("resultFactorial");

const factorial = Calfactorial(number);
resultElement.textContent = factorial;