"use client";
import React, { useState } from 'react'
import { IoAppsSharp } from "react-icons/io5";
import { MdEdit } from "react-icons/md";
import { ColorResult, RGBColor, SketchPicker } from "react-color";
import styles from "./ColorPicker.module.css"; 

const AppSettings = () => {

    { /* Gestion color picker */}
    const [state, setState] = useState({
        displayColorPicker: false,
        color: { r: 255, g: 0, b: 0, a: 1 } as RGBColor
    });

    const handleClick = () => {
        setState({...state, displayColorPicker: !state.displayColorPicker });
      };
    
    const handleClose = () => {
        setState({...state, displayColorPicker: false });
    };

    const handleChange = (color: ColorResult) => {
        setState({
            ...state,
            color: {
                r: color.rgb.r,
                g: color.rgb.g,
                b: color.rgb.b,
                a: color.rgb.a
            } as RGBColor
        });
    };
    

    return (
        <>
            <div className='my-4 mx-6 lg:mx-0 flex items-center border-b-2 border-white w-full'>
                <IoAppsSharp className="mr-2 text-white w-8 h-8 mb-2" />
                <p className='text-xl mb-2'>Informations de l'application</p>
            </div>
            <div>
                <table className="table">
                    <tbody>
                        <tr className="hover">
                            <td className="font-bold">Barre de navigation : prefix</td>
                            <td>
                                <input type="text" placeholder="Type here" className="input input-bordered w-full max-w-xs" />
                            </td>
                            <td>
                                <button className='btn btn-ghost bg-orange-500 hover:bg-orange-600 my-4 ml-4'><MdEdit />Modifier</button>
                            </td>
                        </tr>
                        <tr className="hover">
                            <td className="font-bold">Barre de navigation : couleur</td>
                            <td>
                                <div>
                                    <div className={ styles.swatch } onClick={ handleClick }>
                                        <div className={ styles.color } style={{background: `rgba(${ state.color.r }, ${ state.color.g }, ${ state.color.b }, ${ state.color.a })`}}/>
                                    </div>
                                    { state.displayColorPicker ?
                                        <div className={ styles.popover }>
                                        <div className={ styles.cover } onClick={ handleClose }/>
                                            <SketchPicker color={ state.color } onChange={ handleChange } />
                                        </div> : null
                                    }
                                </div>
                            </td>
                            <td>
                                <button className='btn btn-ghost bg-orange-500 hover:bg-orange-600 my-4 ml-4'><MdEdit />Modifier</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </>
    )
}

export default AppSettings