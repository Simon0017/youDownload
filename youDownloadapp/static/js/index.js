// let card = document.querySelector('div.card');

// function contentPar(datum) {
//     const par = document.createElement('p');
//     const container = document.createElement('div');
//     container.classList.add('card-body');

//     par.classList.add('card-text'),
//     par.textContent = datum;

//     container.appendChild(par);
//     card.appendChild(container);
    
// }

// function Imgaging(datum){
//     const thumnail = document.createElement('img');
    
//     thumnail.classList.add('img-thumbnail img-fluid');
//     thumnail.src = datum;
//     card.appendChild(thumnail);

// }

// switch (data.type) {
//     case 'size':
//         contentPar(data.message);
//         break;

//     case 'speed':
//         contentPar(data.message);
//         break;

//     case 'est':
//         contentPar(data.message);
//         break;

//     case 'error':
//         contentPar(data.message);
//         break;
    
//     case 'thumnail':
//         Imgaging(data.message);
//         break;
//     case 'update':
//         contentPar(data.message);
//         break;
    

//     default:
//         break;
// }