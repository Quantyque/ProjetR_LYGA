import MainMenuChoices from '../../components/MainMenu/MainMenuChoices';


export default function Home() {
  return (
    <>
      <main id='main'>
          <MainMenuChoices number='1' title='RANKING' page='ranking'/>
          <MainMenuChoices number='2' title='PLAYERS' page='players'/>
          <MainMenuChoices number='3' title='TOURNAMENTS' page='tournaments'/>
          <MainMenuChoices number='4' title='COMMUNITY' page='community'/>
          <MainMenuChoices number='5' title='GUIDES' page='guides'/>
          <div className="w-52 rounded-full ring ring-[#191919] ring-offset-[#191919] ring-offset-8" id='MainMenuCircle'>
            <img src="/images/smashMain.png" alt="" />
          </div>
      </main>
    </>
  )
}


