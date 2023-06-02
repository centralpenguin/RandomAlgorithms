class Node
{
public:
	Node(int num)
	{
		val = num;
	}
	int val, l, r;
	Node* left = nullptr, * right = nullptr;
};

Node* build(int l, int r, vector<int>&arr)
{
	if (l > r) return nullptr;
	if (r - l == 0)
	{
		Node *tmp;

		tmp = new Node(arr[l]);
		tmp->l = l;
		tmp->r = r;
		return tmp;
	}
	Node* root = new Node(0);
	int mid = (r + l) / 2;

	root->left = build(l, mid, arr);
	root->right = build(mid + 1, r, arr);
	root->val = min(root->left->val, root->right->val);
	root->l = l;
	root->r = r;
	return root;
}

void print(Node* root, int depth)
{
	if (root == nullptr)
	{
		return;
	}
	cout << depth << " is depth and val is " << root->val << ln;
	print(root->left, depth + 1);
	print(root->right, depth + 1);
}

int minim(Node* root, int levo, int pravo)
{
	if (root->l == levo && root->r == pravo)
	{
		return root->val;
	}
	if (root->l < levo && root->r > pravo)
	{
		int mid = (levo + pravo) / 2;
		int sleva = minim(root->left, levo, mid);
		int sprava = minim(root->right, mid + 1, pravo);
		return min(sleva, sprava);
	}
	
}

int main()
{
	return 0;
}