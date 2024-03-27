let gameName = "bageld"
let num_guesses = 0
let max_guesses = 4;
let success_emoji = "🎾";
let getparams = true
let experimentMessage = '<p>Thanks for playing! bageld is currently in beta, so there are still kinks to work out and there won\'t be daily updates just yet. Check back soon for improvements </p>'

var dropdown = ""
let jsondata = "";
let apiUrl = "https://ci39xriub5.execute-api.us-east-2.amazonaws.com/bagelio_check"

async function getJson(url) {
  let response = await fetch(url);
  let data = await response.json()
  return data;
}


function hashAnswer(string) {
  var hash = 1;
  if (string.length == 0) return hash;
  for (x = 0; x < string.length; x++) {
    ch = string.charCodeAt(x);
    hash = (hash * ch) % 100000000 + 1;
  }
  return hash;
}


// $('select').change(function() {
// // alert("hi");
//     var op =$(this).val();
//     if(op !='') {                 
//     $('input[name="processor_details"]').prop('disabled',false);
// } else {
//     $('input[name="processor_details"]').prop('disabled', true);
// }   
// });

function get_tour_list(atp_wta) {

  const atp_list = [{ value: 'Carlos Alcaraz', text: 'Carlos Alcaraz' },
  { value: 'Novak Djokovic', text: 'Novak Djokovic' },
  { value: 'Daniil Medvedev', text: 'Daniil Medvedev' },
  { value: 'Casper Ruud', text: 'Casper Ruud' },
  { value: 'Stefanos Tsitsipas', text: 'Stefanos Tsitsipas' },
  { value: 'Holger Rune', text: 'Holger Rune' },
  { value: 'Andrey Rublev', text: 'Andrey Rublev' },
  { value: 'Jannik Sinner', text: 'Jannik Sinner' },
  { value: 'Taylor Fritz', text: 'Taylor Fritz' },
  { value: 'Frances Tiafoe', text: 'Frances Tiafoe' },
  { value: 'Karen Khachanov', text: 'Karen Khachanov' },
  { value: 'Aliassime Auger', text: 'Aliassime Auger' },
  { value: 'Cameron Norrie', text: 'Cameron Norrie' },
  { value: 'Borna Coric', text: 'Borna Coric' },
  { value: 'Tommy Paul', text: 'Tommy Paul' },
  { value: 'Lorenzo Musetti', text: 'Lorenzo Musetti' },
  { value: 'Minaur De', text: 'Minaur De' },
  { value: 'Hubert Hurkacz', text: 'Hubert Hurkacz' },
  { value: 'Francisco Cerundolo', text: 'Francisco Cerundolo' },
  { value: 'Pablo Carreno-Busta', text: 'Pablo Carreno-Busta' },
  { value: 'Alexander Zverev', text: 'Alexander Zverev' },
  { value: 'Jan-Lennard Struff', text: 'Jan-Lennard Struff' },
  { value: 'Roberto Bautista-Agut', text: 'Roberto Bautista-Agut' },
  { value: 'Grigor Dimitrov', text: 'Grigor Dimitrov' },
  { value: 'Sebastian Korda', text: 'Sebastian Korda' },
  { value: 'Alexander Bublik', text: 'Alexander Bublik' },
  { value: 'Yoshihito Nishioka', text: 'Yoshihito Nishioka' },
  { value: 'Nicolas Jarry', text: 'Nicolas Jarry' },
  { value: 'Denis Shapovalov', text: 'Denis Shapovalov' },
  { value: 'Daniel Evans', text: 'Daniel Evans' },
  { value: 'Tallon Griekspoor', text: 'Tallon Griekspoor' },
  { value: 'Tomas Etcheverry', text: 'Tomas Etcheverry' },
  { value: 'Nick Kyrgios', text: 'Nick Kyrgios' },
  { value: 'Fokina Davidovich', text: 'Fokina Davidovich' },
  { value: 'Adrian Mannarino', text: 'Adrian Mannarino' },
  { value: 'Ben Shelton', text: 'Ben Shelton' },
  { value: 'Jiri Lehecka', text: 'Jiri Lehecka' },
  { value: 'Matteo Berrettini', text: 'Matteo Berrettini' },
  { value: 'Ugo Humbert', text: 'Ugo Humbert' },
  { value: 'Andy Murray', text: 'Andy Murray' },
  { value: 'Miomir Kecmanovic', text: 'Miomir Kecmanovic' },
  { value: 'Lorenzo Sonego', text: 'Lorenzo Sonego' },
  { value: 'Christopher Eubanks', text: 'Christopher Eubanks' },
  { value: 'De Van', text: 'De Van' },
  { value: 'Yannick Hanfmann', text: 'Yannick Hanfmann' },
  { value: 'Sebastian Baez', text: 'Sebastian Baez' },
  { value: 'Emil Ruusuvuori', text: 'Emil Ruusuvuori' },
  { value: 'Jeffrey Wolf', text: 'Jeffrey Wolf' },
  { value: 'Gregoire Barrere', text: 'Gregoire Barrere' },
  { value: 'Aslan Karatsev', text: 'Aslan Karatsev' },
  { value: 'Anja Stankovic', text: 'Anja Stankovic' },
  { value: 'Yulia Starodubtseva', text: 'Yulia Starodubtseva' },
  { value: 'Stefania Bojica', text: 'Stefania Bojica' },
  { value: 'Wild Seyboth', text: 'Wild Seyboth' },
  { value: 'Goncalo Oliveira', text: 'Goncalo Oliveira' },
  { value: 'Antoine Hoang', text: 'Antoine Hoang' },
  { value: 'Dominic Thiem', text: 'Dominic Thiem' },
  { value: 'Francesco Passaro', text: 'Francesco Passaro' },
  { value: 'Nagi Hanatani', text: 'Nagi Hanatani' },
  { value: 'Reka-Luca Jani', text: 'Reka-Luca Jani' }];

  const wta_list = [{ value: 'Iga Swiatek', text: 'Iga Swiatek' },
  { value: 'Aryna Sabalenka', text: 'Aryna Sabalenka' },
  { value: 'Elena Rybakina', text: 'Elena Rybakina' },
  { value: 'Jessica Pegula', text: 'Jessica Pegula' },
  { value: 'Caroline Garcia', text: 'Caroline Garcia' },
  { value: 'Ons Jabeur', text: 'Ons Jabeur' },
  { value: 'Cori Gauff', text: 'Cori Gauff' },
  { value: 'Maria Sakkari', text: 'Maria Sakkari' },
  { value: 'Petra Kvitova', text: 'Petra Kvitova' },
  { value: 'Darya Kasatkina', text: 'Darya Kasatkina' },
  { value: 'Barbora Krejcikova', text: 'Barbora Krejcikova' },
  { value: 'Veronika Kudermetova', text: 'Veronika Kudermetova' },
  { value: 'Maia Haddad', text: 'Maia Haddad' },
  { value: 'Belinda Bencic', text: 'Belinda Bencic' },
  { value: 'Ludmilla Samsonova', text: 'Ludmilla Samsonova' },
  { value: 'Karolina Muchova', text: 'Karolina Muchova' },
  { value: 'Jelena Ostapenko', text: 'Jelena Ostapenko' },
  { value: 'Madison Keys', text: 'Madison Keys' },
  { value: 'Karolina Pliskova', text: 'Karolina Pliskova' },
  { value: 'Viktoria Azarenka', text: 'Viktoria Azarenka' },
  { value: 'Donna Vekic', text: 'Donna Vekic' },
  { value: 'Ekaterina Alexandrova', text: 'Ekaterina Alexandrova' },
  { value: 'Anastasia Potapova', text: 'Anastasia Potapova' },
  { value: 'Magda Linette', text: 'Magda Linette' },
  { value: 'Qinwen Zheng', text: 'Qinwen Zheng' },
  { value: 'Anhelina Kalinina', text: 'Anhelina Kalinina' },
  { value: 'Bernarda Pera', text: 'Bernarda Pera' },
  { value: 'Elise Mertens', text: 'Elise Mertens' },
  { value: 'Petra Martic', text: 'Petra Martic' },
  { value: 'Irina Begu', text: 'Irina Begu' },
  { value: 'Mayar Sherif', text: 'Mayar Sherif' },
  { value: 'Katerina Siniakova', text: 'Katerina Siniakova' },
  { value: 'Marie Bouzkova', text: 'Marie Bouzkova' },
  { value: 'Lin Zhu', text: 'Lin Zhu' },
  { value: 'Paula Badosa', text: 'Paula Badosa' },
  { value: 'Marta Kostyuk', text: 'Marta Kostyuk' },
  { value: 'Sorana-Mihaela Cirstea', text: 'Sorana-Mihaela Cirstea' },
  { value: 'Shuai Zhang', text: 'Shuai Zhang' },
  { value: 'Sloane Stephens', text: 'Sloane Stephens' },
  { value: 'Anna Blinkova', text: 'Anna Blinkova' },
  { value: 'Varvara Gracheva', text: 'Varvara Gracheva' },
  { value: 'Marketa Vondrousova', text: 'Marketa Vondrousova' },
  { value: 'Elisabetta Cocciaretto', text: 'Elisabetta Cocciaretto' },
  { value: 'Jasmine Paolini', text: 'Jasmine Paolini' },
  { value: 'Linda Noskova', text: 'Linda Noskova' },
  { value: 'Lauren Davis', text: 'Lauren Davis' },
  { value: 'Lucia Bronzetti', text: 'Lucia Bronzetti' },
  { value: 'Camila Giorgi', text: 'Camila Giorgi' },
  { value: 'Shelby Rogers', text: 'Shelby Rogers' },
  { value: 'Bianca Andreescu', text: 'Bianca Andreescu' },
  { value: 'Anja Stankovic', text: 'Anja Stankovic' },
  { value: 'Yulia Starodubtseva', text: 'Yulia Starodubtseva' },
  { value: 'Stefania Bojica', text: 'Stefania Bojica' },
  { value: 'Wild Seyboth', text: 'Wild Seyboth' },
  { value: 'Goncalo Oliveira', text: 'Goncalo Oliveira' },
  { value: 'Antoine Hoang', text: 'Antoine Hoang' },
  { value: 'Dominic Thiem', text: 'Dominic Thiem' },
  { value: 'Francesco Passaro', text: 'Francesco Passaro' },
  { value: 'Nagi Hanatani', text: 'Nagi Hanatani' },
  { value: 'Reka-Luca Jani', text: 'Reka-Luca Jani' }];

  if (atp_wta == 'atp') {
    return atp_list
  }
  else {
    return wta_list
  }
}


async function main() {

  jsondata = await getJson(apiUrl)
  console.log(jsondata);
  console.log('API call successful')

  getparams = false

  let listElems = get_tour_list(jsondata['tour'])

  console.log(listElems)
  dropdown = jSuites.dropdown(document.getElementById('dropdown'), {
    data: listElems,
    width: '280px',
    autocomplete: true,
  });

}

if (getparams) {
  main();
}



function get_guess() {

  var selectedPlayer = dropdown.getValue()
  if (selectedPlayer.length == 0) {
    console.log(selectedPlayer);
  }
  else {
    num_guesses += 1;

    if (hashAnswer(selectedPlayer.toUpperCase()) != jsondata['answerHash']) {
      if (num_guesses == max_guesses) {
        renderFailure()
      }
      else {
        renderNext()

      }
    }
    else {
      renderEnd()
    }
  }

}

function populateHint(numGuesses) {
  var hintContainer = document.getElementById("bagelhint");
  hintContainer.innerHTML = `<img src="https://bagelio-files.s3.us-east-2.amazonaws.com/gifs/mystery_${numGuesses}.gif" width="100%">`
}

function renderNext() {
  var progressContainer = document.getElementById("progress");

  populateHint(num_guesses);
  progressContainer.innerHTML = `<p>${"🟨".repeat(num_guesses) + "⬛️".repeat(max_guesses - num_guesses)
    }</p>`;
}

function renderFailure() {
  var inputSelector = document.getElementById("inputSelector");
  var dropdowndiv = document.getElementById("dropdown");
  var progressContainer = document.getElementById("progress");


  num_guesses += 1

  progressContainer.innerHTML =
    `<p>Sorry, better luck next time</p><p>Share your results: ${"🟨".repeat(
      num_guesses,
    )}</p>`;

  createShareButton();
  inputSelector.remove();
  dropdowndiv.remove();
}

function renderEnd() {
  populateHint(3)
  var inputSelector = document.getElementById("inputSelector");
  var dropdowndiv = document.getElementById("dropdown");
  var progressContainer = document.getElementById("progress");

  progressContainer.innerHTML =
    `<p>You solved it in ${num_guesses} guess${num_guesses > 1 ? "es!" : "! Wow!"
    }</p><p>Share your results: ${"🟨".repeat(
      num_guesses - 1,
    )}${success_emoji}${"🟩".repeat(max_guesses - (num_guesses - 1) - 1)}</p>`;

  createShareButton();

  inputSelector.remove();
  dropdowndiv.remove();
}

function clipboardShare(button) {
  if (num_guesses == max_guesses + 1) {
    var textData = `My ${gameName} score:  \n${"🟨".repeat(
      max_guesses,
    )} \n https://${gameName}.drfronk.com/`;
  } else {
    var textData = `My ${gameName} score:  \n${"🟨".repeat(
      num_guesses - 1,
    )}${success_emoji}${"🟩".repeat(
      max_guesses - (num_guesses - 1) - 1,
    )} \n https://${gameName}.drfronk.com/`;
  }

  navigator.clipboard.writeText(textData).then(() => { button.textContent = "Copied!"; })

  setTimeout(() => {
    button.textContent = "Share";
  }, 700);
}

function createShareButton() {
  const sharebtn = document.querySelector("#sharebtn");
  const button = document.createElement("button");
  button.setAttribute("type", "button");

  button.appendChild(document.createTextNode("Share"));

  button.addEventListener("click", () => {
    clipboardShare(button);
  });

  sharebtn.appendChild(button);
}