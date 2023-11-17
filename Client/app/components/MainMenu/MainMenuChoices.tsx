
"use client"
import { useEffect, useState } from 'react';
import './MainMenuChoices.css';

export default function MainMenuChoices({ number, title, page }: { number: any; title: any; page:any }) {  
  
  
  const [currentGame, setCurrentGame] = useState('smash');
  const [currentIndex, setCurrentIndex] = useState(0);

  const gamesData: { [key: string]: string[] } = {
    smash: [
      "images/smash.jpg",
      "images/smash2.jpg",
      "images/smash3.jpg",
      "images/smash4.jpg",
      "images/smash5.jpg"
    ],
    tekken: [
      "images/tekken.jpg",
      "images/tekken2.jpg",
      "images/tekken3.jpg",
      "images/tekken4.jpg",
      "images/tekken5.jpg"
    ],
    street: [
      "images/street.jpg",
      "images/street2.jpg",
      "images/street3.jpg",
      "images/street4.jpg",
      "images/street5.jpg"
    ],
    mortal: [
      "images/mortal.jpg",
      "images/mortal2.jpg",
      "images/mortal3.jpg",
      "images/mortal4.jpg",
      "images/mortal5.jpg"
    ]
  };

  useEffect(() => {
    const interval = setInterval(() => {
      setCurrentIndex((prevIndex) => (prevIndex + 1) % 5);
      const gameKeys = Object.keys(gamesData);
      const randomGame =
        gameKeys[Math.floor(Math.random() * gameKeys.length)];
      setCurrentGame(randomGame);
    }, 1500); 

    return () => {
      clearInterval(interval); 
    };
  }, []);

  useEffect(() => {
    const gameImages = gamesData[currentGame] || [];
    const imgId = `img${currentIndex + 1}`;
    const imageUrl = gameImages[currentIndex] || '';
    const imgElement = document.getElementById(imgId);
    if (imgElement) {
      imgElement.style.backgroundImage = `url(${imageUrl})`;
    }
  }, [currentGame, currentIndex]);
  
  
  const handleHover = (imgId: string) => {
    const div = document.getElementById('MainMenuCircle');
    if (div) {
      div.style.border = "4px solid";

      // Définir la couleur en fonction de l'ID de l'image
      switch (imgId) {
        case 'img1':
          div.style.borderColor = 'red';
          break;
        case 'img2':
          div.style.borderColor = 'blue';
          break;
        case 'img3':
          div.style.borderColor = 'yellow';
          break;
        case 'img4':
          div.style.borderColor = 'green';
          break;
        case 'img5':
          div.style.borderColor = 'purple';
          break;
        default:
          div.style.borderColor = '#191919';
      }
    }
  };

  const handleMouseOut = () => {
    const div = document.getElementById('MainMenuCircle');
    if (div) {
      div.style.border = "4px solid"
      div.style.borderColor = '#191919'; 
    }
  };

  return (
      <>
        <a href= {`./${page}`} className="vertical-div" id={`img${number}`} onMouseOver={() => handleHover(`img${number}`)}
        onMouseOut={handleMouseOut}>
          <div className="vertical-div-container" id={`colorContainer${number}`}>
            <div className="text-container">
              {title}
            </div>
          </div>
        </a>
      </>
    );
  }
  