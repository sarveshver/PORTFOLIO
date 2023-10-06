var tl =gsap.timeline({scrollTrigger:{
    trigger:"#main",
    markers:true,
    start:"50% 50%",
    end:"100% 50%",
    scrub:2,
    pin:true
}});
tl
.to("#top",{
    top:"-50%"
},'a')
.to("#bottom",{
    bottom:"-50%"
},'a')
.to(".content",{
    marrginTop:"0%"
},'a')
const cursor = document.querySelector('.custom-cursor');

document.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX;
    const mouseY = e.clientY;

    cursor.style.transform = `translate(${mouseX}px, ${mouseY}px)`;
});

