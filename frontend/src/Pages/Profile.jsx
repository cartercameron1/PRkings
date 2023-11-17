import { useParams } from "react-router-dom"
import { useEffect, useState } from "react"

export function Profile() {

    let userId = useParams()
    console.log(userId)

    const [userData, setUserData] = useState({})

    useEffect(() => {
        async function grabData() {
            let data = await fetch("http://127.0.0.1:8000/users/get_user/?id=69", {
                method:"get",
                headers: new Headers({
                    'Content-Type':'application/json',
                }),
            })
            setUserData(data)
        }

        grabData()
    }, [])

    return (
        <>
            {JSON.stringify(userData)}
        </>
    )
}