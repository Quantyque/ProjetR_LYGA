import Link from 'next/link';
import './Ranking.css'

/**
 * Composant de la page de classement
 * @param place palce du joueur
 * @param user_profile image du joueur
 * @param name nom du joueur
 * @param score score du joueur
 * @param idPlayer identifiant du joueur
 * @returns HTML du classement
 * @author Antoine Richard
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
    <tr className={`test ${placePodiumClasse}`} id={`${placePodiumID}`}>
        <th className='text-7xl font-bold text-center'>{place}</th>
        <td>
            <div className="avatar">
                <div className="w-20 rounded-full ring ring-black ring-offset-base-100">
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