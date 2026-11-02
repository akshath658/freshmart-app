import React from "react";

const TaglineSection = () => {
  return (
    <div className="card tagline-card">
      <h2>About FreshMart</h2>
      <p className="tagline-text">
        Your one-stop shop for fresh fruits, vegetables, dairy, and daily essentials.
        Serving the community with the freshest produce delivered daily.
      </p>
      <div className="tagline-features">
        <div className="feature">
          <span>🍎</span>
          <p>Fresh Fruits & Veggies</p>
        </div>
        <div className="feature">
          <span>🥛</span>
          <p>Daily Dairy</p>
        </div>
        <div className="feature">
          <span>🌾</span>
          <p>Staples & Grains</p>
        </div>
        <div className="feature">
          <span>🧴</span>
          <p>Household Items</p>
        </div>
      </div>
    </div>
  );
};

export default TaglineSection;   