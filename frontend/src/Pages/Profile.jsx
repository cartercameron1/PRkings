import { useParams } from "react-router-dom"
import { useEffect, useState } from "react"

export function Profile() {

    let userId = useParams()
    const [userData, setUserData] = useState({})

    useEffect(() => {
        async function grabData() {
            let data = await fetch("http://localhost:8000/users/get_user/?id=69", {
                method:"GET",
                headers: new Headers({
                    'Content-Type':'application/json',
                }),
            })
            let response = await data.json()
            console.log(response)
            setUserData(response)
        }

        grabData()
    }, [])

    return (
        <>
            {JSON.stringify(userData)}
        </>
    )
}