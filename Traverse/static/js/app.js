const appear = document.querySelector('.appear'); 
const cb = function(entries){
entries.forEach(entry => {
    if(entry.isIntersecting){
    entry.target.classList.add('inview');
    }else{
    entry.target.classList.remove('inview');
    }
});
}
const io = new IntersectionObserver(cb);
io.observe(appear);

// homepage laod on-scroll tutorial: https://dev.to/miacan2021/fade-in-animation-on-scroll-with-intersectionobserver-vanilla-js-4p27


const items = document.querySelectorAll('.appear2');

const active = function(entries){
    entries.forEach(entry => {
        if(entry.isIntersecting){
        entry.target.classList.add('inview2'); 
        }else{
            entry.target.classList.remove('inview2'); 
        }
    });
}
const io2 = new IntersectionObserver(active);
 for(let i=0; i < items.length; i++){
    io2.observe(items[i]);
 }