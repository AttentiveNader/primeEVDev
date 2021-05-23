let currentSlide = 0
let holdBack =false
window.setInterval(()=>{
 if (!holdBack){
    if(currentSlide !=2){
        currentSlide +=1 
    }else{
        currentSlide = 0
    }
    let slides = document.querySelectorAll("input[type=radio].slider__nav")
    slides[currentSlide].checked= true
 }
 
},3000)
function Timeout(){
    this.myTimeout = null
    this.settimeout = () => {
        this.iscleared = false
        this.myTimeout =  setTimeout(()=>{holdBack = false},7000)
    }
    this.iscleared = true
    this.clearOut = function(){
        if (!this.iscleared){
            this.iscleared = true
            clearTimeout(this.myTimeout)
        }
    }
}
let t = new Timeout()
function Slide(direction){
    let slides = document.querySelectorAll("input[type=radio].slider__nav")
    if (direction=="left"){
        if(currentSlide !=0){
            currentSlide -=1 
        }else{
            currentSlide = 2
        }

    }else{
        if(currentSlide !=2){
            currentSlide +=1 
        }else{
            currentSlide = 0
        }
    }
    slides[currentSlide].checked= true
    holdBack=true
    if(!t.iscleared){
        t.clearOut()
    }
    t.settimeout()
    // for(let i=0;i<slides.length;i++){
    //     if(slides[i].check){
    //         checkedtab = slides[i]
    //     }
    // }

}