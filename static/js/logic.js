let esTargetEl = document.getElementById("esTarget")
let acTargetEl = document.getElementById("acTarget")
let scoreEl = document.getElementById('score')
let bonusEl = document.getElementById('bonus')
let esVal = 0;
let acVal = 0;
let scoreVal = 0;

esTargetEl.addEventListener("keyup", function(event){
    esVal = parseInt(event.target.value)
    calculateScore()
})
acTargetEl.addEventListener("keyup", function(event){
    acVal = parseInt(event.target.value)
    calculateScore()
})

function calculateScore(){
    if((esVal!==0 && esVal!== NaN) && (acVal!==0 && acVal!==NaN)){
        scoreVal = Math.round(acVal / esVal * 100, 0)
        if (scoreVal >= 100){
            scoreEl.style.color = "green"
            scoreEl.value = 100
            bonusEl.value = parseInt(scoreVal) - 100
            if(bonusEl.value > 0){
                bonusEl.style.color = "green"
            }
        }else{
            bonusEl.style.color="red"
            scoreEl.style.color = "blue"
            scoreEl.value = scoreVal
            bonusEl.value = 0
        }
    }
}

