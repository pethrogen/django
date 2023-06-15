import classes from './EventItem.module.css';

const EventItem = (props) => {

    return (
        <li>
            <div className={classes.event}>
                <h3>{props.name}</h3>
            </div>
        </li>
    );

}

export default EventItem;