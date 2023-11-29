import Link from 'next/link';
import './Ranking.css'

/**
 * Component of "ranking/page.tsx"
 * Show the rank
 * @param place place of a players
 * @param user_profile image of the players
 * @param name name of players
 * @param score score of the players
 * @param idPlayer id of a player
 * @returns the rank of the players from a game and a season
 */
export default function Rank(
    {
        place, 
        user_profile,
        name, 
        team,  
        score,
        idPlayer,
        season_id
    }: 
    {
        place: any; 
        user_profile: any;
        name: any; 
        team: any;
        score: any;
        idPlayer:any;
        season_id:any;
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
        <th className='text-7xl font-bold text-center'>{place}</th>
        <td>
            <div className="avatar">
                <div className="w-20 rounded-full">
                    <img alt="" src={`${user_profile}`}/>
                </div>
            </div>
        </td>
        <td className="text-6xl font-bold">
            {currentTeam}<Link href={{pathname:'/profil',query:{playerId : idPlayer},}}> {name} </Link>
        </td>
        <td className="text-6xl font-bold text-center">{score}</td>
    </tr>
  )
}