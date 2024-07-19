import React, { useState } from 'react';

const CreateAuction = () => {
    const [formData, setFormData] = useState({
        title: '',
        description: '',
        starting_bid: '',
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault()
        console.log('Auction data:', formData);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="title"
                value={formData.title}
                onChange={handleChange}
                placeholder="Title"
            />
            <textarea
                name="description"
                value={formData.description}
                onChange={handleChange}
                placeholder="Description"
            />
            <input
                type="number"
                name="starting_bid"
                value={formData.starting_bid}
                onChange={handleChange}
                placeholder="Starting Bid"
            />
            <button type="submit">Create Auction</button>
        </form>
    );
};

export default CreateAuction;
