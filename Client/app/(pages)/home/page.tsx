import MainMenuChoices from '../../components/MainMenu/MainMenuChoices';
import Navbar from '../../components/Navbar/Navbar';

export default function Home() {
  return (
    <>
      <main id='main'>
          <MainMenuChoices number='1' title='COMMUNITY' page='community'/>
          <MainMenuChoices number='2' title='TOURNAMENTS' page='tournaments'/>
          <MainMenuChoices number='3' title='PLAYERS' page='players'/>
          <MainMenuChoices number='4' title='RANKING' page='ranking'/>
          <MainMenuChoices number='5' title='GUIDES' page='guides'/>
      </main>
    </>
  )
}


