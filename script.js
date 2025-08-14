(function(){
  const form = document.getElementById('birthday-form');
  const input = document.getElementById('birthday');
  const results = document.getElementById('results');
  const weekdayEl = document.getElementById('weekday-born');
  const daysSinceEl = document.getElementById('days-since');
  const daysUntilEl = document.getElementById('days-until');
  const lastBdayLabelEl = document.getElementById('last-bday-label');
  const nextBdayLabelEl = document.getElementById('next-bday-label');
  const ageNextEl = document.getElementById('age-next');
  const daysSinceBirthEl = document.getElementById('days-since-birth');
  const assumptionEl = document.getElementById('assumption');
  const nowEl = document.getElementById('now');
  const resetBtn = document.getElementById('reset');

  const DAY_MS = 24*60*60*1000;

  const fmt = new Intl.DateTimeFormat(undefined, { dateStyle: 'full' });
  const fmtWeekday = new Intl.DateTimeFormat(undefined, { weekday: 'long' });

  function updateClock(){
    nowEl.textContent = new Date().toLocaleString();
  }
  updateClock();
  setInterval(updateClock, 1000);

  function parseInputDate(value){
    // HTML date input gives YYYY-MM-DD. Create a local Date at midnight local time.
    const [y,m,d] = value.split('-').map(Number);
    if(!y||!m||!d) return null;
    const dt = new Date(y, m-1, d, 0,0,0,0);
    // Guard invalid dates like 2021-02-30
    if(dt.getFullYear()!==y || dt.getMonth()!==m-1 || dt.getDate()!==d) return null;
    return dt;
  }

  function isLeapYear(year){
    return (year%4===0 && year%100!==0) || (year%400===0);
  }

  function nextBirthday(baseBirth, today){
    // baseBirth: actual birth date; today: current date
    const month = baseBirth.getMonth();
    const day = baseBirth.getDate();

    let year = today.getFullYear();
    let nb = new Date(year, month, day, 0,0,0,0);

    // Handle Feb 29 birthdays: choose Feb 29 on leap years, Feb 28 on non-leap years
    if(month===1 && day===29){
      if(!isLeapYear(year)) nb = new Date(year, 1, 28, 0,0,0,0);
    }

    if(nb < stripTime(today)){
      year += 1;
      nb = new Date(year, month, day, 0,0,0,0);
      if(month===1 && day===29 && !isLeapYear(year)) nb = new Date(year, 1, 28, 0,0,0,0);
    }
    return nb;
  }

  function lastBirthday(baseBirth, today){
    const month = baseBirth.getMonth();
    const day = baseBirth.getDate();

    let year = today.getFullYear();
    let lb = new Date(year, month, day, 0,0,0,0);
    if(month===1 && day===29 && !isLeapYear(year)) lb = new Date(year, 1, 28, 0,0,0,0);

    if(lb > stripTime(today)){
      year -= 1;
      lb = new Date(year, month, day, 0,0,0,0);
      if(month===1 && day===29 && !isLeapYear(year)) lb = new Date(year, 1, 28, 0,0,0,0);
    }
    return lb;
  }

  function stripTime(d){
    return new Date(d.getFullYear(), d.getMonth(), d.getDate());
  }

  function diffDays(a,b){
    return Math.round((stripTime(a).getTime() - stripTime(b).getTime())/DAY_MS);
  }

  function calc(){
    const value = input.value;
    if(!value){
      results.classList.add('hidden');
      return;
    }

    const birth = parseInputDate(value);
    if(!birth){
      results.classList.add('hidden');
      alert('Please enter a valid date.');
      return;
    }

    const today = new Date();
    const todayStripped = stripTime(today);

    const nb = nextBirthday(birth, todayStripped);
    const lb = lastBirthday(birth, todayStripped);

    const daysUntil = diffDays(nb, todayStripped);
    const daysSince = diffDays(todayStripped, lb);

  const weekday = fmtWeekday.format(birth);
  const totalSinceBirth = diffDays(todayStripped, birth);

    weekdayEl.textContent = weekday;
    daysSinceEl.textContent = daysSince.toString();
    daysUntilEl.textContent = daysUntil.toString();
    lastBdayLabelEl.textContent = `Last birthday: ${fmt.format(lb)}`;
    nextBdayLabelEl.textContent = `Next birthday: ${fmt.format(nb)}`;

    const ageNext = nb.getFullYear() - birth.getFullYear();
    ageNextEl.textContent = ageNext.toString();
  daysSinceBirthEl.textContent = totalSinceBirth.toString();

    // Note for Feb 29 handling
    if(birth.getMonth()===1 && birth.getDate()===29){
      const msg = `You were born on Feb 29. In non-leap years, we use Feb 28 for calculations.`;
      assumptionEl.textContent = msg;
    } else {
      assumptionEl.textContent = '';
    }

    results.classList.remove('hidden');
  }

  form.addEventListener('submit', (e)=>{e.preventDefault();calc();});
  input.addEventListener('change', calc);
  resetBtn.addEventListener('click', ()=>{
    input.value = '';
    results.classList.add('hidden');
    assumptionEl.textContent = '';
    input.focus();
  });
})();
