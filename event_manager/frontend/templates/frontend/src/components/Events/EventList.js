import classes from './EventList.module.css';
import EventItem from './EventItem';

const EventList = (props) => {

    const getItems = (items) => {
        let eventList = [];
        eventList = items.map(item =>
            <EventItem
                name={item.name}
            />
        )
        return eventList;
    }

    return (
        <section className={classes.events}>
            <ul>
                {getItems(props.events)}
            </ul>
        </section>
    );

}

export default EventList;