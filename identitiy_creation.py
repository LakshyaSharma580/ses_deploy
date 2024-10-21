import argparse
import boto3

# Initialize the SES client
ses_client = boto3.client('ses', region_name='us-west-2')  # Adjust region as needed

def create_email_identity(email):
    try:
        response = ses_client.verify_email_identity(EmailAddress=email)
        print(f"Verification email sent to {email}. Response: {response}")
    except Exception as e:
        print(f"Error verifying email identity: {str(e)}")

def create_domain_identity(domain):
    try:
        response = ses_client.verify_domain_identity(Domain=domain)
        print(f"Verification started for domain: {domain}. Response: {response}")
    except Exception as e:
        print(f"Error verifying domain identity: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create SES identities (email or domain).")
    parser.add_argument('--email', type=str, help='Email identity to verify')
    parser.add_argument('--domain', type=str, help='Domain identity to verify')
    
    args = parser.parse_args()

    if args.email:
        create_email_identity(args.email)

    if args.domain:
        create_domain_identity(args.domain)

    if not args.email and not args.domain:
        print("No email or domain identity provided.")
