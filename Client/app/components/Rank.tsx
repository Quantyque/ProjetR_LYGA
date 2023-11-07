import Link from 'next/link';
import '../(pages)/ranking/Ranking.css'

export default function Rank(
    { 
        place, 
        user_profile,
        name, 
        team,  
        score,
        idPlayer
    }: 
    {
        place: any; 
        user_profile: any;
        name: any; 
        team: any;
        score: any;
        idPlayer:any;
    }) 
{

    let placePodiumID;
    let placePodiumClasse;

    if(place == 1){
        placePodiumID = 'firstPlace';
        placePodiumClasse = 'null';
    }
    else if(place == 2){
        placePodiumID = 'secondPlace';
        placePodiumClasse = 'null';
    }
    else if(place == 3){
        placePodiumID = 'thirdPlace';
        placePodiumClasse = 'null';
    }
    else{
        placePodiumID = 'null';
        placePodiumClasse = 'defaultPlace';
    }

    if(user_profile == ''){
        user_profile = '/images/undefined_profile_image.jpg';
    }

    let currentTeam = team + ' | ';

    if(team === null || team === ''){
        currentTeam = "";
    }

  return (
    <tr className={`${placePodiumClasse}`} id={`${placePodiumID}`}>
        <th className='placeRank text-3xl sm:text-6xl'>{place}</th>
        <td>
            <div className="avatar">
                <div className="w-16 rounded-full">
                    <img alt="" src={`${user_profile}`}/>
                </div>
            </div>
        </td>
        <td className='text-xs sm:text-5xl' id='team_Name'>
            {currentTeam}<Link href={{pathname:'/profil',query:{playerId : idPlayer},}}> {name} </Link>
        </td>
        <td className='score text-xs sm:text-5xl'>{score}</td>
    </tr>
  )
}