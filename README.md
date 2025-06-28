# Akedly Python Client

**Akedly Client** is an unofficial Python wrapper for the [Akedly OTP API](https://akedly.io). It provides a simple interface for managing OTP transactions including creation, activation, and verification using Akedly's [Transaction-Based OTP Verification API](https://docs.akedly.io/docs/category/otp-verification).

## About Akedly

[Akedly](https://akedly.io) is a robust authentication-as-a-service platform that offers OTP delivery pipelines for secure user verification via phone or email. This client integrates directly with their public OTP API.

## Features

- Create OTP transactions
- Activate OTP sessions
- Verify OTP codes
- Lightweight with minimal dependencies (requests and python-dotenv)
- Designed for integration into Python-based backend systems

## Installation

```bash
pip install akedly-client
```

## Configuration

This client requires three environment variables. You can load them using a `.env` file and `python-dotenv`.

### Environment Variables

Create a `.env` file in your project root:

```env
AKEDLY_API_URL=https://api.akedly.io/api/v1/transactions
AKEDLY_API_KEY=your_akedly_api_key_here
AKEDLY_PIPELINE_ID=your_pipeline_id_here
```

**Important:** Never commit your `.env` file to version control.

## Usage

```python
from akedly_client import (
    create_otp_transaction,
    activate_otp_transaction,
    verify_otp
)

# 1. Create a new OTP transaction
transaction_id = create_otp_transaction(
    phone="+201234567890",
    email="user@example.com"
)

# 2. Activate the transaction to send OTP
request_id = activate_otp_transaction(transaction_id)

# 3. Verify the OTP entered by the user
is_valid, result = verify_otp(request_id, otp="123456")

if is_valid:
    print("OTP verified successfully.")
else:
    print("Verification failed:", result)
```

## API Reference

For detailed API documentation, please refer to:

- [OTP API Reference](https://docs.akedly.io/docs/category/otp-verification)
- [Akedly Website](https://akedly.io)
- [Dashboard Login](https://dashboard.akedly.io)

## Requirements

- Python 3.7 or higher
- `requests`
- `python-dotenv`

Install dependencies:

```bash
pip install -r requirements.txt
```

## Testing

```bash
pytest tests/
```

Add your test cases under `tests/test_client.py`.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Disclaimer

This is an **unofficial client** maintained by the community. It is not affiliated with Akedly Inc., and no guarantees are provided for uptime, API changes, or SLA adherence.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

For issues related to this client, please open an issue on GitHub. For Akedly API support, please contact Akedly directly through their official channels.
