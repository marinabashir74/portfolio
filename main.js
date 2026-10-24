(function(){
  document.documentElement.classList.add('js');
  const menuBtn=document.querySelector('[data-menu-button]');
  const mobilePanel=document.querySelector('[data-mobile-panel]');
  function setMenu(open){if(!menuBtn||!mobilePanel)return;menuBtn.setAttribute('aria-expanded',String(open));menuBtn.textContent=open?'Close ✕':'Menu ☰';mobilePanel.classList.toggle('open',open);document.body.classList.toggle('menu-open',open)}
  if(menuBtn){menuBtn.addEventListener('click',()=>setMenu(menuBtn.getAttribute('aria-expanded')!=='true'));document.addEventListener('keydown',e=>{if(e.key==='Escape')setMenu(false)});mobilePanel?.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>setMenu(false)))}
  const filters=document.querySelectorAll('[data-filter]');
  const projects=document.querySelectorAll('[data-project-category]');
  const status=document.querySelector('[data-filter-status]');
  filters.forEach(btn=>btn.addEventListener('click',()=>{
    const key=btn.dataset.filter;let visible=0;
    filters.forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));
    projects.forEach(card=>{const show=key==='all'||card.dataset.projectCategory.split(' ').includes(key);card.hidden=!show;if(show)visible++});
    if(status)status.textContent=`Showing ${visible} project${visible===1?'':'s'}`;
  }));
  const serviceSelect=document.getElementById('contact-service');
  if(serviceSelect && window.location.search){
    const params=new URLSearchParams(window.location.search);
    const svc=params.get('service');
    if(svc){
      for(const opt of serviceSelect.options){
        if(opt.value===svc || opt.textContent.includes(svc)){serviceSelect.value=opt.value;break}
      }
    }
  }
  const reveal=document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    const obs=new IntersectionObserver((entries)=>{entries.forEach(x=>{if(x.isIntersecting){x.target.classList.add('in-view');obs.unobserve(x.target)}})},{threshold:.09,rootMargin:'0px 0px -35px 0px'});reveal.forEach(e=>obs.observe(e));
  }else{reveal.forEach(e=>e.classList.add('in-view'))}
  const tilt=document.querySelector('[data-tilt]');
  if(tilt && window.matchMedia('(hover:hover) and (min-width:901px) and (prefers-reduced-motion:no-preference)').matches){
    const parent=tilt.parentElement;parent.addEventListener('pointermove',e=>{const r=parent.getBoundingClientRect();const x=(e.clientX-r.left)/r.width-.5;const y=(e.clientY-r.top)/r.height-.5;tilt.style.transform=`translate(${x*8}px,${y*8}px) rotate(${3+x*2}deg)`});parent.addEventListener('pointerleave',()=>{tilt.style.transform=''})
  }
})();
