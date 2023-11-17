import { useState, useEffect } from "react"
import { submitLift } from "../data/api"

export function SubmitLift() {

    const [liftType, setLiftType] = useState()
    const [liftWeight, setLiftWeight] = useState()
    const [videoSubmission, setVideoSubmission] = useState()
    const [error, setError] = useState("")

    const liftOptions = ["Bench Press", "Squat", "Deadlift"]

    function handleSubmit() {
        console.log(liftType)
        console.log(liftWeight)
        console.log(videoSubmission)
        if (!(liftType && liftWeight && videoSubmission)) {
            alert("All fields must be completed")
            return
        }

        let submitObject = {}
        submitObject.liftType = liftType
        submitObject.liftWeight = liftWeight
        submitObject.video = videoSubmission



        submitLift(submitObject)
    }

    function handleChange(e) {
        setVideoSubmission(e.target.files[0])
    }

    return (
        <>
            <div className="flex flex-col">
                <select value={liftType}>
                    {liftOptions.map((lift) => {
                        return (
                            <option>{lift}</option>
                        )
                    })}
                </select>
                <input placeholder="Lift Amount" className="m-2" onChange={(e) => setLiftWeight(e.target.value)}/>
                <input type="file" onChange={(e) => handleChange(e)} className="m-2"/>
                <button onClick={handleSubmit} className="m-2 p-2 bg-green-600">Submit</button>
            </div>
        </>
    )
}