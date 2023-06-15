/*
Events.js lädt die Events von der API
und stellt eine Funktion zum Hinzufügen
eines Events zur Verfügung
*/
import React, { useState, useEffect, useCallback } from 'react';
import spinner from '../../assets/spinner.gif';
import EventList from './EventList';

const Events = (props) => {
    const url = "/api/event/";

    const [events, setEvents] = useState([]);
    const [isLoading, setIsLoading] = useState(false);

    // asynchrone Anfrage an den Server
    const fetchEventHandler = useCallback(async () => {
        setIsLoading(true);
        try {
            const response = await fetch(url);
            console.log(response);

            if (!response.ok) {
                throw new Error("Something went wrong!");
            }
            const data = await response.json();
            console.log(data);
            setEvents(data);

        } catch (error) {
            console.log("Es gab einen Fehler: ", error.message);
        }
        setIsLoading(false);
    });

    useEffect(() => {
        fetchEventHandler();
    }, []);

    return (
        <div>
            {isLoading ? <img width="50" src={spinner} /> : ""}
            <EventList events={events} />
        </div>
    );
}

export default Events;